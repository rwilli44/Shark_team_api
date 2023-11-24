from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


class Theme(Base):
    __tablename__ = "theme"
    id_theme: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_theme: Mapped[str] = mapped_column(String(255))
    ouvrages: Mapped["Ouvrage"] = relationship(
        secondary="theme_ouvrage", back_populates="themes"
    )
