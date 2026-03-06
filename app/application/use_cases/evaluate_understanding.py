"""
Use case: evaluate user understanding of a competitive programming problem.

Orchestrates the domain and infrastructure: receives DTOs, builds domain entities,
calls the evaluation service, and returns the result. Single responsibility:
application flow for the "evaluate understanding" feature.
"""

import logging

from app.domain.entities.problem import Problem
from app.domain.entities.user_answer import UserAnswer
from app.domain.services.evaluation_service import (
    EvaluationResult,
    EvaluationService,
)

logger = logging.getLogger(__name__)


class EvaluateUnderstandingUseCase:
    """
    Application use case that evaluates if the user understood the problem.

    Depends on the EvaluationService abstraction (DIP). The concrete
    implementation (e.g. PydanticAI) is injected from the infrastructure.
    """

    def __init__(self, evaluation_service: EvaluationService) -> None:
        self._evaluation_service = evaluation_service

    def execute(
        self,
        problem_raw: dict,
        resposta_usuario: dict,
    ) -> EvaluationResult:
        """
        Execute the evaluation flow.

        Args:
            problem_raw: Raw JSON of the problem (titulo, descricao, objetivo, etc.).
            resposta_usuario: Dict with keys ideia, interpretacao_entrada, interpretacao_saida.

        Returns:
            EvaluationResult with result "CORRETO" or "ERRADO". When "ERRADO",
            pedagogical_feedback is filled for internal logging / future feedback agent.
        """
        problem = Problem(problem_raw)
        user_answer = UserAnswer(
            ideia=str(resposta_usuario.get("ideia", "")),
            interpretacao_entrada=str(resposta_usuario.get("interpretacao_entrada", "")),
            interpretacao_saida=str(resposta_usuario.get("interpretacao_saida", "")),
        )
        logger.info(
            "Evaluating understanding for problem %s",
            problem.titulo or "(no title)",
        )
        result = self._evaluation_service.evaluate(problem=problem, user_answer=user_answer)
        if result.pedagogical_feedback:
            logger.info(
                "Pedagogical feedback generated (result=ERRADO): problema_na_interpretacao=%s",
                result.pedagogical_feedback.problema_na_interpretacao[:80],
            )
        return result
