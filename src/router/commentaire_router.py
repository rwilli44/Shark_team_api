from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import ENGINE
from models.commentaire import Commentaire
from schema.commentaire_schema import Commentaire_schema
from datetime import datetime


router = APIRouter()


@router.get("/commentaires/{id_commentaire}", tags=["commentaires"])
async def read_comment(id_commentaire: int):
    with Session(ENGINE) as session:
        stmt = select(Commentaire).where(Commentaire.id_commentaire == id_commentaire)
        result = session.execute(stmt)
        return result


@router.put("/commentaires/add", tags=["commentaires"])
async def add_comment(commentaire: Commentaire_schema):
    with Session(ENGINE) as session:
        new_commentaire = Commentaire(**commentaire.dict())

        session.add_all([new_commentaire])
        session.commit()
        return {"commentaire ajouté": new_commentaire}


#  date_publication_commentaire: Mapped[Date] = mapped_column(Date())
#     contenu_commentaire: Mapped[str] = mapped_column(String(255))
#     titre_commentaire: Mapped[str] = mapped_column(String(255))
#     id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
#     id_ouvrage: Mapped[int]
# with Session(ENGINE) as session:
#     stmt = select(Commentaire).where(Commentaire.id_commentaire == id_commentaire)
#     result = session.execute(stmt)
#     return result
