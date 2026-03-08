"""
Port for code execution and evaluation (Judge).

Implementations call external judge APIs; domain only defines the contract.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class JudgeResult:
    """
    Result of submitting code to the judge.

    Attributes:
        passed: True if all tests passed.
        feedback: Optional message (e.g. error summary).
        failed_cases: Optional list of failed case info for LLM correction (Etapa 3).
            When reveal_inputs is False (Etapa 5), inputs are not included.
    """

    passed: bool
    feedback: str | None = None
    failed_cases: list[dict[str, Any]] | None = None


class JudgePort(ABC):
    """Port for submitting code and getting test results."""

    @abstractmethod
    def submit(
        self,
        code: str,
        language: str,
        problem_id: str,
        *,
        reveal_inputs: bool = False,
    ) -> JudgeResult:
        """
        Submit code for the given problem and language.

        Args:
            code: Source code to run.
            language: Language identifier (e.g. python3, cpp).
            problem_id: Problem identifier for test cases.
            reveal_inputs: If True, failed_cases may include inputs (for LLM retry).
                If False, do not reveal inputs to the user (Etapa 5).
        """
        ...
