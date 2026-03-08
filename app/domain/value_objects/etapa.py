"""
Value object representing a Polya step (etapa).

Used to identify which stage context belongs to and to route orchestration.
"""

from enum import IntEnum


class Etapa(IntEnum):
    """Polya methodology stages (1–5)."""

    COMPREENSAO = 1
    PLANEJAMENTO = 2
    IMPLEMENTACAO_LLM = 3
    IMPLEMENTACAO_USUARIO = 4
    TESTES_USUARIO = 5
