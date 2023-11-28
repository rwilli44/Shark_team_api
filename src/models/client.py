# Third party imports
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# Local imports
from .base import Base


class Client(Base):
    """Classe pour créer le table client et les objets pour représenter
    les lignes du table qui contient tous les clients de la librairie
    et leurs données nécessaires pour les achats."""

    __tablename__ = "client"

    id_client: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_client: Mapped[str] = mapped_column(String(255))
    prenom_client: Mapped[str] = mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[str] = mapped_column(String(20))
    preferences_client: Mapped[str] = mapped_column(String(255))
    adresse_livraison_client: Mapped[str] = mapped_column(String(255))
    adresse_facturation_client: Mapped[str] = mapped_column(String(255))
