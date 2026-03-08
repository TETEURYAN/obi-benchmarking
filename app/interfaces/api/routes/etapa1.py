"""
FastAPI routes for Etapa 1 — Compreensão (Pólya).

POST /etapa1/compreensao: receive problem data + user answers, run comprehension
agent, persist context, return JSON (questao + perguntas).
"""

import logging

from fastapi import APIRouter, HTTPException, status

from app.interfaces.api.schemas import Etapa1CompreensaoRequest, Etapa1CompreensaoResponse
from app.interfaces.api.dependencies import get_etapa1_comprehension_use_case

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/etapa1", tags=["Etapa 1 — Compreensão"])


@router.post(
    "/compreensao",
    response_model=Etapa1CompreensaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Etapa 1 — Compreensão",
    description="Avalia as respostas do usuário às 4 perguntas de compreensão e retorna resumo da questão + feedback por pergunta.",
)
def etapa1_compreensao(body: Etapa1CompreensaoRequest) -> Etapa1CompreensaoResponse:
    """
    Run comprehension agent, save context and return structured output.

    - Validates request via Pydantic.
    - Calls Etapa1ComprehensionUseCase (PydanticAI agent + repository).
    - Returns the same JSON stored as etapa 1 context.
    """
    try:
        use_case = get_etapa1_comprehension_use_case()
        output = use_case.execute(
            id_questao=body.id_questao,
            id_usuario=body.id_usuario,
            descricao_questao=body.descricao_questao,
            formato_entrada=body.formato_entrada,
            formato_saida=body.formato_saida,
            exemplos=body.exemplos,
            respostas_usuario=body.respostas_usuario,
        )
        return Etapa1CompreensaoResponse(
            questao=output["questao"],
            perguntas=output["perguntas"],
        )
    except ValueError as e:
        logger.warning("Validation error in etapa1/compreensao: %s", e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        ) from e
    except Exception as e:
        logger.exception("Etapa 1 comprehension error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Serviço de compreensão temporariamente indisponível. Tente novamente.",
        ) from e
