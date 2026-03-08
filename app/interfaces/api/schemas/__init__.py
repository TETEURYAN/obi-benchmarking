"""API request/response schemas."""

from app.interfaces.api.schemas.etapa1 import (
    Etapa1CompreensaoRequest,
    Etapa1CompreensaoResponse,
)
from app.interfaces.api.schemas.judge import JudgeSubmitRequest, JudgeSubmitResponse
from app.interfaces.api.schemas.legacy import (
    ProblemUnderstandingRequest,
    ProblemUnderstandingResponse,
    RespostaUsuarioSchema,
)

__all__ = [
    "Etapa1CompreensaoRequest",
    "Etapa1CompreensaoResponse",
    "JudgeSubmitRequest",
    "JudgeSubmitResponse",
    "ProblemUnderstandingRequest",
    "ProblemUnderstandingResponse",
    "RespostaUsuarioSchema",
]
