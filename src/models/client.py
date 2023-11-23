from base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Client(Base):
    __tablename__ = "client"

    id_client: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_client: Mapped[str] = mapped_column(String(255))
    prenom_client: Mapped[str] = mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[str] = mapped_column(String(20))
    preferences_client: Mapped[str] = mapped_column(String(255))
    adresse_livraison_client: Mapped[str] = mapped_column(String(255))
    adresse_facturation_client: Mapped[str] = mapped_column(String(255))
