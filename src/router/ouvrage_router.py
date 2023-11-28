from fastapi import APIRouter, HTTPException
from schema.ouvrage_schema import Ouvrage_schema, Ouvrage_schema_optionnel
from sqlalchemy.orm import Session
from models.ouvrage import Ouvrage
from config.connexion import ENGINE


router = APIRouter()


##### Read #####
@router.get("/ouvrages/{id_ouvrage}", tags=["ouvrage"],summary="Donne les informations en fonction de l'id ouvrage",description="Saisir l'id ouvrage pour en voir les informations")
async def get_ouvrage(
    id_ouvrage_get: int,
):
    with Session(ENGINE) as session:
        ouvrage_db = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_get).first()
        )
        if ouvrage_db:
            return ouvrage_db
    raise HTTPException(status_code=404, detail="L'ouvrage n'a pas pu être retrouvé.")


##### Create #####
@router.post(
    "/ouvrage/",
    response_model=Ouvrage_schema,
    tags=["ouvrage"],
    summary="Création d'un ouvrage",description="Saisir les champs spécifiques à la création de l'ouvrage"
)
async def create_ouvrage(ouvrage: Ouvrage_schema):
    with Session(ENGINE) as session:
        ouvrage_model = Ouvrage(**ouvrage.dict())
        session.add_all([ouvrage_model])
        session.commit()
        return Ouvrage_schema.from_orm(ouvrage_model)


##### Update #####
@router.patch("/ouvrage/{id_ouvrage}", response_model=Ouvrage_schema, tags=["ouvrage"], summary="Mise à jour de l'ouvrage selectionné via l'id",description="Changement du champs qui est nécessaire, les autres champs peuvent être supprimés et garderont leur ancienne valeur")
async def update_ouvrage(id_ouvrage_up: int, ouvrage: Ouvrage_schema_optionnel):
    with Session(ENGINE) as session:
        db_ouvrage = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_up).first()
        )
        if db_ouvrage:
            for key, value in ouvrage.dict(exclude_unset=True).items():
                setattr(db_ouvrage, key, value)
            session.commit()
            session.refresh(db_ouvrage)
        return Ouvrage_schema.from_orm(db_ouvrage)


##### Delete #####
@router.delete("/ouvrage/{id_ouvrage}", tags=["ouvrage"],summary="Effacement d'un ouvrage via son id",description="Saisir l'id pour le supprimer")
async def delete_ouvrage(id_ouvrage_get: int):
    with Session(ENGINE) as session:
        ouvrage_db = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_get).first()
        )
        if ouvrage_db:
            session.delete(ouvrage_db)
            session.commit()
            return {"Ouvrage supprimé: ": ouvrage_db}

##### Read #####
@router.get("/recherche/{critere_tri}&{nom}", tags=["recherche"],summary="Recherche à double paramètre",description="Rentrer dans la première variable le type de recherche que vous voulez faire (auteur, thème, ...) et remplire dans la deuxième variable le nom associé")
async def get_recherche(critere : str, nom : str):
    with Session(ENGINE) as session:
        if critere == "auteur":
            ouvrage_db = (session.query(Ouvrage).filter(Ouvrage.auteur_ouvrage == nom))
        if ouvrage_db:
            return ouvrage_db
    raise HTTPException(status_code=404, detail="L'ouvrage n'a pas pu être retrouvé.")
