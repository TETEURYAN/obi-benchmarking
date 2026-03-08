"""
Use case: Etapa 1 — Compreensão (Pólya).

Receives problem data + user answers to the 4 comprehension questions,
calls the comprehension agent, persists context and returns the structured output.
"""

import logging
from typing import Any

from app.domain.ports.agents.comprehension import (
    ComprehensionAgentPort,
    ComprehensionInput,
    ComprehensionOutput,
)
from app.domain.ports.repositories.etapa_context_repository import EtapaContextRepository
from app.domain.entities.etapa_context import EtapaContext
from app.domain.value_objects import Etapa

logger = logging.getLogger(__name__)


class Etapa1ComprehensionUseCase:
    """
    Application use case for Etapa 1 (Comprehension).

    Depends on ComprehensionAgentPort and EtapaContextRepository (DIP).
    """

    def __init__(
        self,
        comprehension_agent: ComprehensionAgentPort,
        etapa_context_repository: EtapaContextRepository,
    ) -> None:
        self._agent = comprehension_agent
        self._repo = etapa_context_repository

    def execute(
        self,
        id_questao: str,
        id_usuario: str,
        descricao_questao: str,
        formato_entrada: str,
        formato_saida: str,
        exemplos: Any,
        respostas_usuario: dict[str, str],
    ) -> ComprehensionOutput:
        """
        Run comprehension agent and persist context for Etapa 1.

        Returns the same JSON that is stored as context (questao + perguntas).
        """
        input_data: ComprehensionInput = {
            "descricao_questao": descricao_questao,
            "formato_entrada": formato_entrada,
            "formato_saida": formato_saida,
            "exemplos": exemplos,
            "respostas_usuario": respostas_usuario,
        }
        output = self._agent.run(input_data)
        # Persist as etapa 1 context
        context_entity = EtapaContext(
            etapa=Etapa.COMPREENSAO,
            id_questao=id_questao,
            id_usuario=id_usuario,
            contexto=dict(output),
        )
        self._repo.save(context_entity)
        logger.info(
            "Etapa 1 context saved for question=%s user=%s",
            id_questao,
            id_usuario,
        )
        return output
