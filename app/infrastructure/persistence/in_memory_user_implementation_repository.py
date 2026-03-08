"""
In-memory implementation of UserImplementationRepository.

Stores LLM code (after E3), Etapa 4 records and Etapa 5 results.
"""

from app.domain.entities.user_implementation import UserImplementation, UserTestResult
from app.domain.ports.repositories.user_implementation_repository import UserImplementationRepository


class InMemoryUserImplementationRepository(UserImplementationRepository):
    """In-memory store for user implementation and test results."""

    def __init__(self) -> None:
        self._codigo_llm: dict[tuple[str, str], str] = {}  # (id_questao, id_usuario) -> code
        self._etapa4: list[UserImplementation] = []
        self._etapa5: list[UserTestResult] = []

    def save_codigo_llm_etapa3(self, id_questao: str, id_usuario: str, codigo_llm: str) -> None:
        self._codigo_llm[(id_questao, id_usuario)] = codigo_llm

    def save_etapa4(self, record: UserImplementation) -> None:
        self._etapa4.append(record)

    def save_etapa5(self, record: UserTestResult) -> None:
        self._etapa5.append(record)

    def get_codigo_llm(self, id_questao: str, id_usuario: str) -> str | None:
        return self._codigo_llm.get((id_questao, id_usuario))
