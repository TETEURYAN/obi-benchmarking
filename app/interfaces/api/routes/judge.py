"""
FastAPI routes for Judge (submissão de código).

POST /judge/submit: envia código para o judge externo e retorna passed, feedback e failed_cases.
Exemplo de uso: Etapa 3 (código LLM) e Etapa 5 (código do usuário).
"""

import logging

from fastapi import APIRouter, HTTPException, status

from app.domain.ports.judges.judge import JudgePort
from app.interfaces.api.dependencies import get_judge
from app.interfaces.api.schemas.judge import JudgeSubmitRequest, JudgeSubmitResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/judge", tags=["Judge"])


@router.post(
    "/submit",
    response_model=JudgeSubmitResponse,
    status_code=status.HTTP_200_OK,
    summary="Submeter código ao Judge",
    description="Envia código para o judge externo. Retorna se passou, feedback e (opcional) casos falhos.",
)
def judge_submit(body: JudgeSubmitRequest) -> JudgeSubmitResponse:
    """
    Chama o JudgePort (ExternalJudgeAdapter) e devolve o resultado.

    - Valida body via Pydantic.
    - Usa get_judge() para obter a implementação (configurada em settings).
    - Retorna passed, feedback e failed_cases conforme contrato do domínio.
    """
    try:
        judge: JudgePort = get_judge()
        result = judge.submit(
            code=body.code,
            language=body.language,
            problem_id=body.problem_id,
            reveal_inputs=body.reveal_inputs,
        )
        return JudgeSubmitResponse(
            passed=result.passed,
            feedback=result.feedback,
            failed_cases=result.failed_cases,
        )
    except Exception as e:
        logger.exception("Judge submit error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Judge temporariamente indisponível. Tente novamente.",
        ) from e
