"""
PydanticAI-based implementation of the Comprehension Agent (Etapa 1).

Uses structured output (Pydantic model) to guarantee the JSON shape required
by the domain (ComprehensionOutput).
"""

import json
import logging
from typing import Any

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from app.config.settings import get_settings
from app.domain.ports.agents.comprehension import (
    ComprehensionAgentPort,
    ComprehensionInput,
    ComprehensionOutput,
)
from app.infrastructure.prompts.versions import load_prompt

logger = logging.getLogger(__name__)


# ----- Pydantic models for PydanticAI structured output -----


class QuestaoResumoModel(BaseModel):
    """Resumo da questão no output do agente."""

    descricao: str = Field(description="Descrição simplificada do problema")
    entrada_problema: str = Field(description="Formato/resumo da entrada")
    saida_problema: str = Field(description="Formato/resumo da saída esperada")


class PerguntaAvaliacaoModel(BaseModel):
    """Avaliação de uma pergunta."""

    status: str = Field(description="correto ou errado")
    feedback: str = Field(description="Feedback curto ao usuário")


class ComprehensionOutputModel(BaseModel):
    """Output estruturado do agente de compreensão."""

    questao: QuestaoResumoModel
    perguntas: dict[str, PerguntaAvaliacaoModel] = Field(
        description="Chave: texto da pergunta. Valor: status e feedback."
    )


def _output_to_dict(model: ComprehensionOutputModel) -> ComprehensionOutput:
    """Convert Pydantic model to TypedDict-compatible dict."""
    return {
        "questao": {
            "descricao": model.questao.descricao,
            "entrada_problema": model.questao.entrada_problema,
            "saida_problema": model.questao.saida_problema,
        },
        "perguntas": {
            k: {"status": v.status, "feedback": v.feedback}
            for k, v in model.perguntas.items()
        },
    }


class PydanticAIComprehensionAgent(ComprehensionAgentPort):
    """
    Comprehension agent implemented with PydanticAI.

    Loads system prompt from versioned prompts (v1 by default); model from settings.
    """

    def __init__(self, model: str | None = None, prompt_version: str = "v1") -> None:
        self._model = model or get_settings().llm_model
        self._prompt_version = prompt_version
        system_prompt = load_prompt(prompt_version, "comprehension")
        self._agent = Agent(
            self._model,
            output_type=ComprehensionOutputModel,
            system_prompt=system_prompt,
        )

    def run(self, input_data: ComprehensionInput) -> ComprehensionOutput:
        """Run the agent and return domain ComprehensionOutput."""
        message = json.dumps(input_data, ensure_ascii=False, indent=2)
        try:
            result = self._agent.run_sync(message)
        except Exception as e:
            logger.exception("Comprehension agent run failed: %s", e)
            raise
        return _output_to_dict(result.output)
