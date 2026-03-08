"""
Orchestrator for the Polya methodology flow.

Coordinates use cases and repositories: loads previous stage context when needed,
calls the appropriate use case, and decides next step (e.g. after E3 judge pass
→ allow user implementation).
"""

import logging
from typing import Any

from app.domain.ports.repositories.etapa_context_repository import EtapaContextRepository
from app.domain.ports.repositories.user_implementation_repository import UserImplementationRepository
from app.domain.value_objects import Etapa

logger = logging.getLogger(__name__)


class PolyaOrchestrator:
    """
    Orchestrator for the five Polya stages.

    Does not depend on agents or judge directly; use cases are invoked by the
    API layer with the right dependencies. The orchestrator can hold references
    to use cases or only to repositories for loading context (minimal design).
    """

    def __init__(
        self,
        etapa_context_repository: EtapaContextRepository,
        user_implementation_repository: UserImplementationRepository,
    ) -> None:
        self._context_repo = etapa_context_repository
        self._impl_repo = user_implementation_repository

    def get_context_etapa1(self, id_questao: str, id_usuario: str) -> dict[str, Any] | None:
        """Load Etapa 1 context for use in Etapa 2 or 3."""
        return self._context_repo.load(Etapa.COMPREENSAO, id_questao, id_usuario)

    def get_context_etapa2(self, id_questao: str, id_usuario: str) -> dict[str, Any] | None:
        """Load Etapa 2 context for use in Etapa 3."""
        return self._context_repo.load(Etapa.PLANEJAMENTO, id_questao, id_usuario)

    def get_codigo_llm(self, id_questao: str, id_usuario: str) -> str | None:
        """Get LLM-generated code for Etapa 4 analysis."""
        return self._impl_repo.get_codigo_llm(id_questao, id_usuario)
