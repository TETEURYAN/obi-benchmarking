"""
Port for the Implementation Agent (Etapa 3 — Pólya).

Receives context from Etapa 1 + Etapa 2 + chosen language;
returns full solution code. Judge is called outside this port.
"""

from abc import ABC, abstractmethod
from typing import Any, TypedDict


class ImplementationInput(TypedDict, total=False):
    """Input for the implementation agent."""

    contexto_etapa1: dict[str, Any]
    contexto_etapa2: dict[str, Any]
    linguagem: str


class ImplementationOutput(TypedDict):
    """Output: code only."""

    codigo: str


class ImplementationAgentPort(ABC):
    """Port for the Etapa 3 implementation agent (LLM generates code)."""

    @abstractmethod
    def run(self, input_data: ImplementationInput) -> ImplementationOutput:
        """Generate solution code from context and language."""
        ...
