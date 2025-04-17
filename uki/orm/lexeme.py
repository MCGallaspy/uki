from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy.types import String
from typing import Optional, List, Set

from uki.orm.base import UkiʔBase


class Lexeme(UkiʔBase):
    __tablename__ = "lexeme"

    id: Mapped[int] = mapped_column(primary_key=True)
    lemma: Mapped[str] = mapped_column(String(256))
    morpheme_type: Mapped[Optional[str]] = mapped_column(String(256))
    
    surface_forms: Mapped[Set["SurfaceForm"]] = relationship(back_populates="lexeme")
    senses: Mapped[Set["Sense"]] = relationship(back_populates="lexeme")
    
    def __repr__(self):
        return f"Lexeme(id={self.id}, lemma='{self.lemma}', morpheme_type='{self.morpheme_type}')"