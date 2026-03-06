"""
Domain service interface for evaluating user understanding.

This abstraction (D in SOLID) allows the application layer to depend on
an evaluation capability without depending on a specific LLM implementation.
The infrastructure layer will provide the concrete implementation (e.g. PydanticAI).
"""

from abc import ABC, abstractmethod
from typing import Literal

from app.domain.entities.problem import Problem
from app.domain.entities.user_answer import UserAnswer


EvaluationResultType = Literal["CORRETO", "ERRADO"]


class PedagogicalFeedback:
    """
    Structured pedagogical feedback when the user's understanding is incorrect.

    Used internally for logging and for the future feedback agent; not returned
    in the HTTP response.
    """

    __slots__ = (
        "problema_na_interpretacao",
        "conceitos_mal_compreendidos",
        "correcao_conceitual",
        "dica_para_resolver",
    )

    def __init__(
        self,
        problema_na_interpretacao: str,
        conceitos_mal_compreendidos: str,
        correcao_conceitual: str,
        dica_para_resolver: str,
    ) -> None:
        self.problema_na_interpretacao = problema_na_interpretacao
        self.conceitos_mal_compreendidos = conceitos_mal_compreendidos
        self.correcao_conceitual = correcao_conceitual
        self.dica_para_resolver = dica_para_resolver


class EvaluationResult:
    """
    Result of evaluating the user's understanding.

    Attributes:
        result: Either "CORRETO" or "ERRADO".
        pedagogical_feedback: Present only when result is "ERRADO"; contains
            structured feedback for internal use / future feedback agent.
    """

    __slots__ = ("result", "pedagogical_feedback")

    def __init__(
        self,
        result: EvaluationResultType,
        pedagogical_feedback: PedagogicalFeedback | None = None,
    ) -> None:
        self.result = result
        self.pedagogical_feedback = pedagogical_feedback


class EvaluationService(ABC):
    """
    Port for evaluating whether a user correctly understood a problem.

    Implementations (e.g. LLM-based) live in the infrastructure layer.
    """

    @abstractmethod
    def evaluate(
        self,
        problem: Problem,
        user_answer: UserAnswer,
    ) -> EvaluationResult:
        """
        Evaluate if the user's understanding matches the problem.

        Args:
            problem: The structured problem statement.
            user_answer: The user's ideia, interpretacao_entrada, interpretacao_saida.

        Returns:
            EvaluationResult with result "CORRETO" or "ERRADO". When "ERRADO",
            pedagogical_feedback is populated for internal use.
        """
        ...
