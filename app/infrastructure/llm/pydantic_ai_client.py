"""
PydanticAI-based implementation of the evaluation service.

Provides two agents:
1. Evaluation agent: returns CORRETO or ERRADO based on user understanding.
2. Feedback agent: when ERRADO, generates structured pedagogical feedback
   for internal use (logging / future feedback agent).

Designed so the LLM model can be swapped via config (get_settings().llm_model).
"""

import json
import logging
import os
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from app.config.settings import get_settings
from app.domain.entities.problem import Problem
from app.domain.entities.user_answer import UserAnswer
from app.domain.services.evaluation_service import (
    EvaluationResult,
    EvaluationService,
    PedagogicalFeedback,
)

logger = logging.getLogger(__name__)


# ----- Structured output models for PydanticAI -----


class EvaluationOutput(BaseModel):
    """Output type for the evaluation agent: exactly CORRETO or ERRADO."""

    result: Literal["CORRETO", "ERRADO"] = Field(
        description="Avaliação: CORRETO ou ERRADO"
    )


class PedagogicalFeedbackOutput(BaseModel):
    """Output type for the pedagogical feedback agent."""

    problema_na_interpretacao: str = Field(
        description="O que está incorreto na interpretação do usuário"
    )
    conceitos_mal_compreendidos: str = Field(
        description="Quais conceitos do problema foram mal compreendidos"
    )
    correcao_conceitual: str = Field(
        description="Como corrigir o entendimento conceitual"
    )
    dica_para_resolver: str = Field(
        description="Passo a passo ou dica para chegar à interpretação correta"
    )


# ----- Prompts -----

EVALUATION_SYSTEM_PROMPT = """Você é um avaliador de compreensão de problemas de programação competitiva.

Sua tarefa é avaliar se o usuário entendeu corretamente o problema descrito.

Critérios de avaliação (todos devem ser atendidos para CORRETO):
1. O usuário entendeu o objetivo do problema.
2. O usuário interpretou corretamente o formato e significado da entrada.
3. O usuário interpretou corretamente o formato e significado da saída esperada.
4. O usuário identificou os conceitos algorítmicos envolvidos (quando aplicável).
5. O usuário não cometeu erros conceituais graves.

Você receberá:
- O enunciado estruturado do problema (objetivo, entrada, saída, restrições, exemplos).
- A interpretação do usuário: ideia geral, interpretação da entrada e da saída.

Responda EXATAMENTE com um único valor: CORRETO ou ERRADO.
- CORRETO: apenas se a compreensão estiver correta e completa.
- ERRADO: se houver qualquer equivoco na interpretação do objetivo, entrada, saída ou conceitos."""

FEEDBACK_SYSTEM_PROMPT = """Você é um tutor de programação competitiva.

O usuário interpretou INCORRETAMENTE um problema. Gere um feedback pedagógico estruturado em português:

1. problema_na_interpretacao: descreva objetivamente o que está incorreto na interpretação.
2. conceitos_mal_compreendidos: liste quais conceitos do problema foram mal compreendidos.
3. correcao_conceitual: explique como corrigir o entendimento (o que revisar).
4. dica_para_resolver: dê um passo a passo ou dicas para chegar à interpretação correta.

Seja claro, objetivo e didático. O feedback será usado por outro agente para ajudar o usuário."""


def _build_message(problem: Problem, user_answer: UserAnswer) -> str:
    """Build the user message containing problem and user answer for the LLM."""
    payload = {
        "problema": problem.raw,
        "resposta_usuario": {
            "ideia": user_answer.ideia,
            "interpretacao_entrada": user_answer.interpretacao_entrada,
            "interpretacao_saida": user_answer.interpretacao_saida,
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _log_llm_error(exc: Exception, step: str) -> None:
    """Log LLM failure and hint at API key when relevant."""
    logger.exception("LLM %s request failed: %s", step, exc)
    err_str = str(exc).lower()
    if "api_key" in err_str or "401" in err_str or "authentication" in err_str:
        logger.info("Hint: set OPENAI_API_KEY in .env and restart the service.")


class PydanticAIEvaluationService(EvaluationService):
    """
    Evaluation service implementation using PydanticAI agents.

    Uses two agents: one for evaluation (CORRETO/ERRADO), one for pedagogical
    feedback when the result is ERRADO. The feedback is stored internally
    and not returned in the HTTP response.
    """

    def __init__(self, model: str | None = None) -> None:
        """
        Initialize with optional model override. If not provided, uses settings.llm_model.
        """
        self._model = model or get_settings().llm_model
        self._warn_if_openai_key_missing()
        self._evaluation_agent = Agent(
            self._model,
            output_type=EvaluationOutput,
            system_prompt=EVALUATION_SYSTEM_PROMPT,
        )
        self._feedback_agent = Agent(
            self._model,
            output_type=PedagogicalFeedbackOutput,
            system_prompt=FEEDBACK_SYSTEM_PROMPT,
        )

    def _warn_if_openai_key_missing(self) -> None:
        if self._model.strip().lower().startswith("openai"):
            if not os.environ.get("OPENAI_API_KEY", "").strip():
                logger.warning(
                    "LLM is %s but OPENAI_API_KEY is not set. Set it in .env and restart.",
                    self._model,
                )

    def evaluate(
        self,
        problem: Problem,
        user_answer: UserAnswer,
    ) -> EvaluationResult:
        """
        Evaluate user understanding via LLM; if ERRADO, generate pedagogical feedback.
        """
        message = _build_message(problem, user_answer)

        try:
            run_result = self._evaluation_agent.run_sync(message)
        except Exception as e:
            _log_llm_error(e, "evaluation")
            raise

        output: EvaluationOutput = run_result.output
        result_value = output.result

        if result_value == "CORRETO":
            return EvaluationResult(result="CORRETO")

        # ERRADO: second call to generate pedagogical feedback (internal use only)
        try:
            feedback_run = self._feedback_agent.run_sync(message)
        except Exception as e:
            logger.warning("Pedagogical feedback request failed (result remains ERRADO): %s", e)
            return EvaluationResult(result="ERRADO")

        fb: PedagogicalFeedbackOutput = feedback_run.output
        pedagogical_feedback = PedagogicalFeedback(
            problema_na_interpretacao=fb.problema_na_interpretacao,
            conceitos_mal_compreendidos=fb.conceitos_mal_compreendidos,
            correcao_conceitual=fb.correcao_conceitual,
            dica_para_resolver=fb.dica_para_resolver,
        )
        return EvaluationResult(result="ERRADO", pedagogical_feedback=pedagogical_feedback)
