"""
Port for the Analysis Agent (Etapa 4 — Pólya).

Compares LLM code and user code: compatibility, syntax, consistency.
Returns subtle feedback when there are issues; otherwise ok to send to Judge.
"""

from abc import ABC, abstractmethod
from typing import TypedDict


class AnalysisInput(TypedDict):
    """Input for the analysis agent."""

    codigo_llm: str
    codigo_user: str


class AnalysisOutput(TypedDict):
    """Output of the analysis agent."""

    ok: bool
    feedback: str  # subtle feedback when not ok


class AnalysisAgentPort(ABC):
    """Port for the Etapa 4 analysis agent."""

    @abstractmethod
    def run(self, input_data: AnalysisInput) -> AnalysisOutput:
        """Analyze user code against LLM reference; return ok + feedback."""
        ...
