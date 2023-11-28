# Third party imports
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# Local imports
from .base import Base


class ThemeOuvrage(Base):
    """Classe pour créer le table d'association qui mappe chaque ouvrage
    aux thèmes qu'on trouve dans le livre."""

    __tablename__ = "theme_ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(
        ForeignKey("ouvrage.id_ouvrage"), primary_key=True
    )
    id_theme: Mapped[int] = mapped_column(
        ForeignKey("theme.id_theme"), primary_key=True
    )
