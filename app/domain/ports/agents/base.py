"""
Base port for LLM agents.

Agents receive typed input and return typed output; implementations
can use PydanticAI, LangChain, or any other LLM provider (DIP).
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class AgentPort(ABC, Generic[InputT, OutputT]):
    """Port for a single agent: run with input and return structured output."""

    @abstractmethod
    def run(self, input_data: InputT) -> OutputT:
        """Execute the agent with the given context. Must be deterministic-friendly for tests."""
        ...
