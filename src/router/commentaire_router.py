from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.connexion import ENGINE
from models.commentaire import Commentaire
from schema.commentaire_schema import (
    CommentaireCreate_schema,
    CommentaireRequest_schema,
    CommentaireUpdate_schema,
)
from datetime import date


router = APIRouter()


##### Create #####
@router.post(
    "/commentaires",
    response_model=CommentaireRequest_schema,
    status_code=201,
    tags=["commentaires"],
    summary="Créer un commentaire",
    description="Créer un commentaire - avec : contenu_commentaire: str, titre_commentaire: str, id_client: int, id_ouvrage: int, et date_publication_commentaire: datetime.",
)
async def add_comment(commentaire: CommentaireCreate_schema):
    try:
        with Session(ENGINE) as session:
            new_commentaire = Commentaire(**commentaire.dict())
            session.add_all([new_commentaire])
            session.commit()
            return CommentaireRequest_schema.model_validate(new_commentaire)
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=f"Le commentaire n'a pas pu être ajouté: {str(e)}",
        )


##### Read #####
@router.get(
    "/commentaires/{id_comment}",
    response_model=CommentaireRequest_schema,
    tags=["commentaires"],
    summary="Lire un commentaire",
    description="Lire un commentaire par son ID.",
)
async def read_comment(id_comment: int):
    with Session(ENGINE) as session:
        result = (
            session.query(Commentaire)
            .where(Commentaire.id_commentaire == id_comment)
            .first()
        )
        if result:
            return CommentaireRequest_schema.model_validate(result)
    raise HTTPException(
        status_code=404, detail="Le commentaire n'a pas pu être retrouvé."
    )


##### Update #####
@router.patch(
    "/commentaires/{id_to_update}",
    response_model=CommentaireRequest_schema,
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
            session.refresh(db_commentaire)
            return CommentaireRequest_schema.model_validate(db_commentaire)
        raise HTTPException(
            status_code=404, detail="Le commentaire n'a pas pu être mise à jour."
        )


##### Delete #####
@router.delete(
    "/commentaires/{id_to_delete}",
    status_code=201,
    tags=["commentaires"],
    summary="Supprimer un commentaire",
    description="Supprimer définitivement un commentaire - à utiliser judicieusement.",
)
async def delete_commentaire(id_to_delete: int):
    with Session(ENGINE) as session:
        comment_to_delete = (
            session.query(Commentaire).filter_by(id_commentaire=id_to_delete).first()
        )
        if comment_to_delete:
            session.delete(comment_to_delete)
            session.commit()
            return "Commentaire supprimé."
    raise HTTPException(
        status_code=404, detail="Le commentaire n'a pas pu être trouvé."
    )
