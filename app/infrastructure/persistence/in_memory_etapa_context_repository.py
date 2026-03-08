"""
In-memory implementation of EtapaContextRepository.

Used for development and tests. Replace with a PostgreSQL implementation
for production (e.g. SQLAlchemy in infrastructure/persistence/).
"""

from typing import Any

from app.domain.entities.etapa_context import EtapaContext
from app.domain.ports.repositories.etapa_context_repository import EtapaContextRepository
from app.domain.value_objects import Etapa


class InMemoryEtapaContextRepository(EtapaContextRepository):
    """Stores etapa context in a dict keyed by (etapa, id_questao, id_usuario)."""

    def __init__(self) -> None:
        self._store: dict[tuple[Etapa, str, str], dict[str, Any]] = {}

    def save(self, context: EtapaContext) -> None:
        key = (context.etapa, context.id_questao, context.id_usuario)
        self._store[key] = context.contexto

    def load(self, etapa: Etapa, id_questao: str, id_usuario: str) -> dict[str, Any] | None:
        key = (etapa, id_questao, id_usuario)
        return self._store.get(key)
