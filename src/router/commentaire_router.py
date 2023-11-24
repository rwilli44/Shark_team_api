from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select
from config.connexion import ENGINE
from models.commentaire import Commentaire
from schema.commentaire_schema import Commentaire_schema
from datetime import datetime


router = APIRouter()

############## GET AND POST OK: delete et patch à faire + tests


@router.get(
    "/commentaires/{id_comment}",
    response_model=Commentaire_schema,
    tags=["commentaires"],
)
async def read_comment(id_comment: int):
    with Session(ENGINE) as session:
        stmt = select(Commentaire).where(Commentaire.id_commentaire == id_comment)
        result = session.scalars(stmt).one()
        return Commentaire_schema.from_orm(result)


@router.post(
    "/commentaires/add", response_model=Commentaire_schema, tags=["commentaires"]
)
async def add_comment(commentaire: Commentaire_schema):
    with Session(ENGINE) as session:
        new_commentaire = Commentaire(**commentaire.module_dump())
        session.add_all([new_commentaire])
        session.commit()
        return Commentaire_schema.from_orm(new_commentaire)


#  date_publication_commentaire: Mapped[Date] = mapped_column(Date())
#     contenu_commentaire: Mapped[str] = mapped_column(String(255))
#     titre_commentaire: Mapped[str] = mapped_column(String(255))
#     id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
#     id_ouvrage: Mapped[int]
# with Session(ENGINE) as session:
#     stmt = select(Commentaire).where(Commentaire.id_commentaire == id_commentaire)
#     result = session.execute(stmt)
#     return result
