"""
Port and data types for the Comprehension Agent (Etapa 1 — Pólya).

Receives problem statement + user answers to the 4 comprehension questions;
returns structured summary and per-question evaluation with feedback.
"""

from abc import ABC, abstractmethod
from typing import Any, TypedDict


class ComprehensionInput(TypedDict, total=False):
    """Input for the comprehension agent."""

    descricao_questao: str
    formato_entrada: str
    formato_saida: str
    exemplos: Any  # list or dict
    respostas_usuario: dict[str, str]  # question -> answer


class QuestaoResumo(TypedDict):
    """Simplified problem summary in agent output."""

    descricao: str
    entrada_problema: str
    saida_problema: str


class PerguntaAvaliacao(TypedDict):
    """Per-question evaluation."""

    status: str  # "correto" | "errado"
    feedback: str


class ComprehensionOutput(TypedDict):
    """Output of the comprehension agent (JSON saved as etapa 1 context)."""

    questao: QuestaoResumo
    perguntas: dict[str, PerguntaAvaliacao]


class ComprehensionAgentPort(ABC):
    """
    Port for the Etapa 1 comprehension agent.

    Implementations use LLM (e.g. PydanticAI) to produce ComprehensionOutput.
    """

    @abstractmethod
    def run(self, input_data: ComprehensionInput) -> ComprehensionOutput:
        """Evaluate user answers and return structured summary + per-question feedback."""
        ...
