from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class ThemeOuvrage(Base):
    __tablename__ = "theme_ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(
        ForeignKey("ouvrage.id_ouvrage"), primary_key=True
    )
    id_theme: Mapped[int] = mapped_column(
        ForeignKey("ouvrage.id_ouvrage"), primary_key=True
    )
