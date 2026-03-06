"""
Domain entity representing the user's interpretation of a problem.

Encapsulates the three fields the user must provide: ideia, interpretacao_entrada
and interpretacao_saida.
"""


class UserAnswer:
    """
    User's understanding of a problem: main idea and input/output interpretation.

    Attributes:
        ideia: User's summary of the problem idea.
        interpretacao_entrada: How the user interprets the input format/meaning.
        interpretacao_saida: How the user interprets the expected output.
    """

    __slots__ = ("_ideia", "_interpretacao_entrada", "_interpretacao_saida")

    def __init__(
        self,
        ideia: str,
        interpretacao_entrada: str,
        interpretacao_saida: str,
    ) -> None:
        self._ideia = ideia
        self._interpretacao_entrada = interpretacao_entrada
        self._interpretacao_saida = interpretacao_saida

    @property
    def ideia(self) -> str:
        return self._ideia

    @property
    def interpretacao_entrada(self) -> str:
        return self._interpretacao_entrada

    @property
    def interpretacao_saida(self) -> str:
        return self._interpretacao_saida

    def __repr__(self) -> str:
        return "UserAnswer(ideia=..., interpretacao_entrada=..., interpretacao_saida=...)"
