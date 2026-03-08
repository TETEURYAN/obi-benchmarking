"""
Domain entity for stage (etapa) context persisted in the database.

Stores the JSON context produced by each Polya stage (e.g. comprehension
summary + per-question feedback for stage 1).
"""

from typing import Any

from app.domain.value_objects import Etapa


class EtapaContext:
    """
    Context saved for a given stage (etapa), question and user.

    Attributes:
        id: Optional persistence id.
        etapa: Stage (1–5).
        id_questao: Problem id.
        id_usuario: User id.
        contexto: JSON-serializable dict (resumo, perguntas, etc.).
    """

    __slots__ = ("_id", "_etapa", "_id_questao", "_id_usuario", "_contexto")

    def __init__(
        self,
        etapa: Etapa,
        id_questao: str,
        id_usuario: str,
        contexto: dict[str, Any],
        id: str | None = None,
    ) -> None:
        self._id = id
        self._etapa = etapa
        self._id_questao = id_questao
        self._id_usuario = id_usuario
        self._contexto = dict(contexto)

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def etapa(self) -> Etapa:
        return self._etapa

    @property
    def id_questao(self) -> str:
        return self._id_questao

    @property
    def id_usuario(self) -> str:
        return self._id_usuario

    @property
    def contexto(self) -> dict[str, Any]:
        return self._contexto.copy()
