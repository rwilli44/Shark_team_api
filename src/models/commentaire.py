from .base import Base
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship


class Commentaire(Base):
    __tablename__ = "commentaire"

    id_commentaire: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date_publication_commentaire: Mapped[Date] = mapped_column(Date())
    auteur_commentaire: Mapped[str] = mapped_column(String(255))
    titre_commentaire: Mapped[str] = mapped_column(String(255))
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
    id_ouvrage: Mapped[int] = mapped_column(ForeignKey("ouvrage.id_ouvrage"))
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="commentaires")
