from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.connexion import ENGINE
from models.commentaire import Commentaire
from schema.commentaire_schema import Commentaire_schema, CommentaireUpdate_schema
from datetime import date


router = APIRouter()


##### Create #####
@router.post(
    "/commentaires/add",
    response_model=Commentaire_schema,
    tags=["commentaires"],
    summary="Créer un commentaire",
    description="Créer un commentaire - avec : contenu_commentaire: str, titre_commentaire: str, id_client: int, id_ouvrage: int, et date_publication_commentaire: datetime.",
)
async def add_comment(commentaire: Commentaire_schema):
    with Session(ENGINE) as session:
        new_commentaire = Commentaire(**commentaire.dict())
        session.add_all([new_commentaire])
        session.commit()
        return Commentaire_schema.model_validate(new_commentaire)
    raise HTTPException(
        status_code=404, detail="Le commentaire n'a pas pu être ajouté."
    )


##### Read #####
@router.get(
    "/commentaires/{id_comment}",
    response_model=Commentaire_schema,
    tags=["commentaires"],
    summary="Lire un commentaire",
    description="Lire un commentaire par son ID.",
)
async def read_comment(id_to_read: int):
    with Session(ENGINE) as session:
        result = (
            session.query(Commentaire)
            .where(Commentaire.id_commentaire == id_to_read)
            .first()
        )
        if result:
            return Commentaire_schema.model_validate(result)
    raise HTTPException(
        status_code=404, detail="Le commentaire n'a pas pu être retrouvé."
    )


##### Update #####
@router.patch(
    "/commentaires/{id_to_update}",
    tags=["commentaires"],
    summary="Mettre à jour un commentaire",
    description="Éditer le titre (titre_commentaire) ou le contenu (contenu_commentaire) d'un Commentaire. La date de publication se met à jour automatiquement.",
)
async def update_commentaire(id_to_update: int, update_data: CommentaireUpdate_schema):
    with Session(ENGINE) as session:
        db_commentaire = (
            session.query(Commentaire)
            .filter(Commentaire.id_commentaire == id_to_update)
            .first()
        )
        if db_commentaire:
            for field, value in update_data.dict(exclude_unset=True).items():
                setattr(db_commentaire, field, value)
            setattr(db_commentaire, "date_publication_commentaire", date.today())
            session.commit()
            updated_comment = (
                session.query(Commentaire)
                .filter(Commentaire.id_commentaire == id_to_update)
                .first()
            )

            return updated_comment
        raise HTTPException(
            status_code=404, detail="Le commentaire n'a pas pu être mise à jour."
        )


##### Delete #####
@router.delete(
    "/commentaires/{id_to_delete}",
    tags=["commentaires"],
    summary="Supprimer un commentaire",
    description="Supprime définitivement un commentaire - à utiliser judicieusement.",
)
async def delete_commentaire(id_to_delete: int):
    with Session(ENGINE) as session:
        comment_to_delete = (
            session.query(Commentaire).filter_by(id_commentaire=id_to_delete).first()
        )
        print(comment_to_delete)
        if comment_to_delete:
            session.delete(comment_to_delete)
            session.commit()
            return "Commentaire supprimé."
    raise HTTPException(
        status_code=404, detail="Le commentaire n'a pas pu être trouvé."
    )
