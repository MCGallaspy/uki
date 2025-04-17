from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from uki.orm.base import UkiʔBase
from uki.orm.lexeme import Lexeme


class SurfaceForm(UkiʔBase):
    __tablename__ = "surface_form"

    id: Mapped[int] = mapped_column(primary_key=True)
    form: Mapped[str] = mapped_column(String(256))
    lexeme_id: Mapped[int] = mapped_column(ForeignKey("lexeme.id"))
    lexeme: Mapped[Lexeme] = relationship(back_populates="surface_forms")
