# Third party imports
from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local imports
from .base import Base


class Commentaire(Base):
    """Classe pour créer le table commentaire et les objets pour représenter
    les lignes du table qui contient tous les commentaires sur les ouvrages
    de la librairie et les lie au client et à l'ouvrage."""

    __tablename__ = "commentaire"

    id_commentaire: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date_publication_commentaire: Mapped[Date] = mapped_column(Date())
    contenu_commentaire: Mapped[str] = mapped_column(String(255))
    titre_commentaire: Mapped[str] = mapped_column(String(255))
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
    id_ouvrage: Mapped[int] = mapped_column(ForeignKey("ouvrage.id_ouvrage"))
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="commentaires")
