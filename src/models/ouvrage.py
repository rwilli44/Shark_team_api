from .base import Base
from sqlalchemy import ForeignKey, String, Date, Numeric
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


class Ouvrage(Base):
    __tablename__ = "ouvrage"

    id_ouvrage: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titre_ouvrage: Mapped[str] = mapped_column(String(255))
    auteur_ouvrage: Mapped[str] = mapped_column(String(255))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20))
    langue_ouvrage: Mapped[str] = mapped_column(String(20))
    prix_ouvrage: Mapped[float] = mapped_column(Numeric)
    date_parution_ouvrage: Mapped[Date] = mapped_column(Date)
    categorie_ouvrage: Mapped[str] = mapped_column(String(255))
    date_disponibilite_libraire_ouvrage: Mapped[Date] = mapped_column(Date)
    date_disponibilite_particulier_ouvrage: Mapped[Date] = mapped_column(Date)
    image_ouvrage: Mapped[str] = mapped_column(String(255))
    table_des_matieres_ouvrage: Mapped[str] = mapped_column(String(255))
    mot_cle_ouvrage: Mapped[str] = mapped_column(String(255))
    description_ouvrage: Mapped[str] = mapped_column(String(255))
    commentaires: Mapped[list["Commentaire"]] = relationship(back_populates="ouvrage")
