"""
Port for the Planning Agent (Etapa 2 — Pólya).

Receives context from Etapa 1 + user answers about strategy and language;
returns evaluation of planning answers.
"""

from abc import ABC, abstractmethod
from typing import Any, TypedDict


class PlanningInput(TypedDict, total=False):
    """Input for the planning agent."""

    contexto_etapa1: dict[str, Any]
    respostas_usuario: dict[str, str]


class PlanningOutput(TypedDict):
    """Output of the planning agent (JSON saved as etapa 2 context)."""

    avaliacao: dict[str, Any]  # structured evaluation of each answer


class PlanningAgentPort(ABC):
    """Port for the Etapa 2 planning agent."""

    @abstractmethod
    def run(self, input_data: PlanningInput) -> PlanningOutput:
        """Evaluate planning answers and return structured evaluation."""
        ...
