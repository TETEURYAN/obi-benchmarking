"""
FastAPI routes for the Problem Understanding Agent.

Single endpoint: POST /evaluate-understanding.
Logging and exception handling are applied at this layer.
"""

import logging

from fastapi import APIRouter, HTTPException, status

from app.application.use_cases.evaluate_understanding import EvaluateUnderstandingUseCase
from app.infrastructure.llm.pydantic_ai_client import PydanticAIEvaluationService
from app.interfaces.api.schemas import (
    ProblemUnderstandingRequest,
    ProblemUnderstandingResponse,
)
from app.config.settings import get_settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="", tags=["Problem Understanding"])

# Dependency: evaluation service (can be swapped for tests or other LLM impl).
# Cleared on failure so next request gets a fresh instance (avoids stuck cache state).
_evaluation_service: PydanticAIEvaluationService | None = None

SERVICE_UNAVAILABLE_MESSAGE = (
    "Serviço de avaliação temporariamente indisponível. Tente novamente mais tarde."
)


def get_evaluation_service() -> PydanticAIEvaluationService:
    """Return the singleton evaluation service (lazy init for optional DI)."""
    global _evaluation_service
    if _evaluation_service is None:
        _evaluation_service = PydanticAIEvaluationService()
    return _evaluation_service


def _clear_evaluation_service() -> None:
    """Clear singleton so next request creates a new service instance."""
    global _evaluation_service
    _evaluation_service = None
    get_settings.cache_clear()


@router.post(
    "/evaluate-understanding",
    response_model=ProblemUnderstandingResponse,
    status_code=status.HTTP_200_OK,
    summary="Evaluate user understanding",
    description="Avalia se o usuário compreendeu corretamente o problema. Retorna CORRETO ou ERRADO.",
)
def evaluate_understanding(
    body: ProblemUnderstandingRequest,
) -> ProblemUnderstandingResponse:
    """
    Evaluate whether the user correctly understood the problem.

    - Validates request body via Pydantic.
    - Calls the evaluation use case (LLM via PydanticAI).
    - Returns only { "result": "CORRETO" } or { "result": "ERRADO" }.
    - When ERRADO, pedagogical feedback is generated internally and logged.
    """
    try:
        service = get_evaluation_service()
        use_case = EvaluateUnderstandingUseCase(evaluation_service=service)
        evaluation_result = use_case.execute(
            problem_raw=body.problema,
            resposta_usuario=body.resposta_usuario.model_dump(),
        )
        return ProblemUnderstandingResponse(result=evaluation_result.result)
    except ValueError as e:
        logger.warning("Validation error in evaluate-understanding: %s", e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        ) from e
    except Exception as e:
        logger.exception("Evaluation service error (clearing singleton): %s", e)
        _clear_evaluation_service()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=SERVICE_UNAVAILABLE_MESSAGE,
        ) from e
