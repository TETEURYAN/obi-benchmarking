"""Port for persisting user implementation (Etapa 4) and test results (Etapa 5)."""

from abc import ABC, abstractmethod

from app.domain.entities.user_implementation import UserImplementation, UserTestResult


class UserImplementationRepository(ABC):
    """Port for saving Etapa 3 (LLM code), Etapa 4 and Etapa 5 records."""

    @abstractmethod
    def save_codigo_llm_etapa3(self, id_questao: str, id_usuario: str, codigo_llm: str) -> None:
        """Save LLM-generated code after Etapa 3 judge pass (for use in Etapa 4)."""
        ...

    @abstractmethod
    def save_etapa4(self, record: UserImplementation) -> None:
        """Save LLM code, user code and feedback for Etapa 4."""
        ...

    @abstractmethod
    def save_etapa5(self, record: UserTestResult) -> None:
        """Save test run status and optional feedback (no inputs)."""
        ...

    @abstractmethod
    def get_codigo_llm(self, id_questao: str, id_usuario: str) -> str | None:
        """Return LLM-generated code for this problem/user (for Etapa 4 analysis)."""
        ...
