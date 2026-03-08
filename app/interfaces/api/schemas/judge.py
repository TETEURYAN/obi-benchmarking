"""
Request/response schemas for Judge submit endpoint.

Exposes the JudgePort contract at the API boundary.
"""

from typing import Any

from pydantic import BaseModel, Field


class JudgeSubmitRequest(BaseModel):
    """Request body for POST /judge/submit."""

    code: str = Field(..., description="Código fonte a ser avaliado")
    language: str = Field(..., description="Linguagem (ex: python3, cpp)")
    problem_id: str = Field(..., description="Identificador da questão")
    reveal_inputs: bool = Field(
        default=False,
        description="Se True, casos falhos podem incluir inputs (ex: para LLM na Etapa 3)",
    )


class JudgeSubmitResponse(BaseModel):
    """Response body for POST /judge/submit."""

    passed: bool = Field(..., description="True se todos os testes passaram")
    feedback: str | None = Field(default=None, description="Mensagem de feedback (erro ou resumo)")
    failed_cases: list[dict[str, Any]] | None = Field(
        default=None,
        description="Casos que falharam (quando reveal_inputs=True pode incluir inputs)",
    )
