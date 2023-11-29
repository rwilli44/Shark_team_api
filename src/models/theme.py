# Third party imports
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from .base import Base


class Theme(Base):
    """Classe pour créer le table theme et les objets pour représenter
    les lignes du table qui contient tous les thèmes trouvés dans les
    ouvrages de la librairie"""

    __tablename__ = "theme"
    id_theme: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_theme: Mapped[str] = mapped_column(String(255))
    ouvrages: Mapped["Ouvrage"] = relationship(
        secondary="theme_ouvrage", back_populates="themes"
    )
