"""Domain entities."""

from app.domain.entities.problem import Problem
from app.domain.entities.user_answer import UserAnswer
from app.domain.entities.etapa_context import EtapaContext
from app.domain.entities.user_implementation import UserImplementation, UserTestResult

__all__ = [
    "Problem",
    "UserAnswer",
    "EtapaContext",
    "UserImplementation",
    "UserTestResult",
]
