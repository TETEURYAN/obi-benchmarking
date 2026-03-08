"""
Legacy request/response schemas for POST /evaluate-understanding.

Kept for backward compatibility with the existing endpoint.
"""

from typing import Any

from pydantic import BaseModel, Field


class RespostaUsuarioSchema(BaseModel):
    """User's interpretation of the problem (ideia, entrada, saida)."""

    ideia: str = Field(..., description="Ideia geral do usuário sobre o problema")
    interpretacao_entrada: str = Field(
        ...,
        description="Como o usuário interpreta a entrada",
    )
    interpretacao_saida: str = Field(
        ...,
        description="Como o usuário interpreta a saída esperada",
    )


class ProblemUnderstandingRequest(BaseModel):
    """
    Request body for POST /evaluate-understanding.

    Contains the structured problem and the user's answer.
    """

    problema: dict[str, Any] = Field(
        ...,
        description="Enunciado estruturado do problema (titulo, descricao, objetivo, entrada, saida, restricoes, exemplos, etc.)",
    )
    resposta_usuario: RespostaUsuarioSchema = Field(
        ...,
        description="Interpretação do usuário: ideia, interpretacao_entrada, interpretacao_saida",
    )


class ProblemUnderstandingResponse(BaseModel):
    """
    Response body for POST /evaluate-understanding.

    Only two possible values for result: CORRETO or ERRADO.
    """

    result: str = Field(
        ...,
        description="Avaliação da compreensão: CORRETO ou ERRADO",
    )
