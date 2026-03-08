"""Agent ports (domain)."""

from app.domain.ports.agents.base import AgentPort
from app.domain.ports.agents.comprehension import (
    ComprehensionAgentPort,
    ComprehensionInput,
    ComprehensionOutput,
)
from app.domain.ports.agents.planning import PlanningAgentPort, PlanningInput, PlanningOutput
from app.domain.ports.agents.implementation import (
    ImplementationAgentPort,
    ImplementationInput,
    ImplementationOutput,
)
from app.domain.ports.agents.analysis import AnalysisAgentPort, AnalysisInput, AnalysisOutput

__all__ = [
    "AgentPort",
    "ComprehensionAgentPort",
    "ComprehensionInput",
    "ComprehensionOutput",
    "PlanningAgentPort",
    "PlanningInput",
    "PlanningOutput",
    "ImplementationAgentPort",
    "ImplementationInput",
    "ImplementationOutput",
    "AnalysisAgentPort",
    "AnalysisInput",
    "AnalysisOutput",
]
