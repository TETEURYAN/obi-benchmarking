"""
Request/response schemas for Etapa 1 — Compreensão.

Validates input at the API boundary and shapes the response.
"""

from typing import Any

from pydantic import BaseModel, Field


class Etapa1CompreensaoRequest(BaseModel):
    """Request body for POST /etapa1/compreensao."""

    id_questao: str = Field(..., description="Identificador da questão")
    id_usuario: str = Field(..., description="Identificador do usuário")
    descricao_questao: str = Field(..., description="Descrição da questão")
    formato_entrada: str = Field(..., description="Formato da entrada")
    formato_saida: str = Field(..., description="Formato da saída esperada")
    exemplos: Any = Field(default_factory=dict, description="Exemplos de entrada/saída")
    respostas_usuario: dict[str, str] = Field(
        ...,
        description="Respostas às 4 perguntas de compreensão (pergunta -> resposta)",
    )


class Etapa1CompreensaoResponse(BaseModel):
    """
    Response body for POST /etapa1/compreensao.

    Mirrors the JSON saved as context: questao (resumo) + perguntas (status e feedback).
    """

    questao: dict[str, str] = Field(..., description="Resumo: descricao, entrada_problema, saida_problema")
    perguntas: dict[str, dict[str, str]] = Field(
        ...,
        description="Para cada pergunta: { status, feedback }",
    )
