from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.connexion import ENGINE
from models.theme import Theme
from schema.theme_schema import Theme_CreateUpdate_Schema, Theme_Read_Schema

router = APIRouter()


##### Create #####
@router.post(
    "/themes",
    response_model=Theme_Read_Schema,
    status_code=201,
    tags=["thèmes"],
    summary="Créer un thème",
    description="Créer un thème - avec : nom_theme: str.",
)
async def add_theme(new_theme: Theme_CreateUpdate_Schema):
    try:
        with Session(ENGINE) as session:
            theme_object = Theme(**new_theme.dict())
            session.add_all([theme_object])
            session.commit()
            return Theme_Read_Schema.model_validate(theme_object)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"Le thème n'a pas pu être ajouté:{str(e)}."
        )


##### Read #####
# Get 1 thème par ID
@router.get(
    "/themes/{id_to_read}",
    response_model=Theme_Read_Schema,
    tags=["thèmes"],
    summary="Afficher un theme",
    description="Lire un theme par son ID.",
)
async def read_theme(id_to_read: int):
    with Session(ENGINE) as session:
        result = session.query(Theme).where(Theme.id_theme == id_to_read).first()
        if result:
            return Theme_Read_Schema.model_validate(result)
    raise HTTPException(status_code=404, detail="Le thème n'a pas pu être retrouvé.")


# Get tous les thèmes disponibles
@router.get(
    "/themes/all/",
    tags=["thèmes"],
    summary="Get tous les thèmes",
    description="Retourne un objet JSON avec tous les thèmes disponibles",
)
async def read_themes():
    with Session(ENGINE) as session:
        results = session.query(Theme).all()
        if results:
            return results
    raise HTTPException(status_code=404, detail="Aucun thème n'a été retrouvé.")


##### Update #####
@router.patch(
    "/themes/{id_to_update}",
    response_model=Theme_CreateUpdate_Schema,
    tags=["thèmes"],
    summary="Mettre à jour un thème",
    description="Éditer le nom du thème (nom_theme)",
)
async def update_theme(id_to_update: int, update_data: Theme_CreateUpdate_Schema):
    with Session(ENGINE) as session:
        db_theme = session.query(Theme).filter(Theme.id_theme == id_to_update).first()
        if db_theme:
            for field, value in update_data.dict(exclude_unset=True).items():
                setattr(db_theme, field, value)
            session.commit()
            session.refresh(db_theme)
            return Theme_Read_Schema.model_validate(db_theme)
        raise HTTPException(
            status_code=404, detail="Le thème n'a pas pu être mis à jour."
        )


##### Delete #####
@router.delete(
    "/themes/{id_to_delete}",
    tags=["thèmes"],
    summary="Supprimer un thème",
    description="Supprimer définitivement un thème - à utiliser judicieusement.",
)
async def delete_theme(id_to_delete: int):
    with Session(ENGINE) as session:
        theme_to_delete = session.query(Theme).filter_by(id_theme=id_to_delete).first()
        print(theme_to_delete)
        if theme_to_delete:
            session.delete(theme_to_delete)
            session.commit()
            return "Thème supprimé."
    raise HTTPException(status_code=404, detail="Le thème n'a pas pu être trouvé.")
