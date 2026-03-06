"""
Domain entity representing a competitive programming problem.

This entity is agnostic of transport and persistence; it holds the core
data that describes a problem statement. The structure is flexible to
accommodate the full enunciado estruturado from the platform.
"""

from typing import Any


class Problem:
    """
    Represents a competitive programming problem with its full structured statement.

    Attributes:
        raw: The complete problem payload (titulo, descricao, objetivo,
             entrada, saida, restricoes, pontuacao, conceitos_envolvidos,
             exemplos, etc.) as received from the platform.
    """

    __slots__ = ("_raw",)

    def __init__(self, raw: dict[str, Any]) -> None:
        """
        Build a Problem from the raw structured JSON.

        Args:
            raw: Dictionary containing titulo, descricao, objetivo, entrada,
                 saida, restricoes, pontuacao, conceitos_envolvidos, exemplos, etc.
        """
        self._raw = dict(raw)

    @property
    def raw(self) -> dict[str, Any]:
        """Immutable view of the raw problem data."""
        return self._raw.copy()

    @property
    def titulo(self) -> str:
        """Problem title."""
        return str(self._raw.get("titulo", ""))

    def __repr__(self) -> str:
        return f"Problem(titulo={self.titulo!r})"
