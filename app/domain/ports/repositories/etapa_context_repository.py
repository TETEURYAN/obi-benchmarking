"""Port for persisting and loading etapa context (stages 1–5)."""

from abc import ABC, abstractmethod
from typing import Any

from app.domain.entities.etapa_context import EtapaContext
from app.domain.value_objects import Etapa


class EtapaContextRepository(ABC):
    """Port for saving and loading stage context by etapa, question and user."""

    @abstractmethod
    def save(self, context: EtapaContext) -> None:
        """Persist context (upsert by etapa + id_questao + id_usuario)."""
        ...

    @abstractmethod
    def load(self, etapa: Etapa, id_questao: str, id_usuario: str) -> dict[str, Any] | None:
        """Load context as dict; None if not found."""
        ...
