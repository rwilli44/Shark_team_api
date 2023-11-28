# Third party imports
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

# Local imports
from config.connexion import ENGINE
from models.commentaire import Commentaire
from models.ouvrage import Ouvrage
from schema.ouvrage_schema import Ouvrage_schema, Ouvrage_schema_optionnel


router = APIRouter()


##### Create #####
@router.post(
    "/ouvrage/",
    response_model=Ouvrage_schema,
    tags=["ouvrage"],
    summary="Création d'un ouvrage",
    description="Saisir les champs spécifiques à la création de l'ouvrage",
)
async def create_ouvrage(ouvrage: Ouvrage_schema):
    try:
        with Session(ENGINE) as session:
            ouvrage_model = Ouvrage(**ouvrage.dict())
            session.add_all([ouvrage_model])
            session.commit()
            return Ouvrage_schema.from_orm(ouvrage_model)
    except Exception as e:
        raise HTTPException(
            status_code=422, detail=f"L'ouvrage n'a pas pu être ajouté:{str(e)}."
        )


##### Read #####
# Recherche d'ouvre par ID
@router.get(
    "/ouvrages/{id_ouvrage_get}",
    tags=["ouvrage"],
    summary="Donne les informations en fonction de l'id ouvrage",
    description="Saisir l'id ouvrage pour en voir les informations",
)
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


##### recherche unitaire #####
@router.get(
    "/recherche_unitaire/{critere}/{nom}",
    tags=["recherche"],
    summary="Recherche suivant un attribut",
    description="Rentrer dans le critère de recherche soit auteur, soit catégorie, soit langue, soit mot clé ou titre. Ensuite  rentrer le nom que vous souhaitez afin de chercher dans la base de données",
)
async def recherche_unitaire(critere: str, nom: str):
    with Session(ENGINE) as session:
        dic_critere = {
            "auteur": Ouvrage.auteur_ouvrage,
            "catégorie": Ouvrage.categorie_ouvrage,
            "langue": Ouvrage.langue_ouvrage,
            "mot clé": Ouvrage.mot_cle_ouvrage,
            "titre": Ouvrage.titre_ouvrage,
        }

        for cle, valeur in dic_critere.items():
            if cle == critere:
                ouvrage_db = (session.query(Ouvrage).filter(valeur.contains(nom))).all()
                return ouvrage_db

    raise HTTPException(status_code=404, detail="Aucun ouvrage n'a pu être trouvé.")


##### recherche double critère #####
@router.get(
    "/recherche_double/{critere1}/{nom1}/{critere2}/{nom2}",
    tags=["recherche"],
    summary="Recherche suivant deux attributs",
    description="Rentrer dans les critères de recherche soit auteur, soit catégorie, soit langue, soit mot clé. Ensuite  rentrer les noms que vous souhaitez afin de chercher dans la base de données",
)
async def recherche_double(critere1: str, nom1: str, critere2: str, nom2: str):
    with Session(ENGINE) as session:
        dic_critere = {
            "auteur": Ouvrage.auteur_ouvrage,
            "catégorie": Ouvrage.categorie_ouvrage,
            "langue": Ouvrage.langue_ouvrage,
            "mot clé": Ouvrage.mot_cle_ouvrage,
            "titre": Ouvrage.titre_ouvrage,
        }

        query = session.query(Ouvrage)
        for cle, valeur in dic_critere.items():
            if cle == critere1:
                query = query.filter(valeur.contains(nom1))
            if cle == critere2:
                query = query.filter(valeur.contains(nom2))
        ouvrage_db = query.all()
    if ouvrage_db:
        return ouvrage_db
    raise HTTPException(status_code=404, detail="Aucun ouvrage n'a pu être trouvé.")


##### Update #####
@router.patch(
    "/ouvrage/{id_ouvrage_up}",
    response_model=Ouvrage_schema,
    tags=["ouvrage"],
    summary="Mise à jour de l'ouvrage selectionné via l'id",
    description="Changement du champs qui est nécessaire, les autres champs peuvent ne pas être envoyés et garderont leur ancienne valeur",
)
async def update_ouvrage(id_ouvrage_up: int, ouvrage_update: Ouvrage_schema_optionnel):
    with Session(ENGINE) as session:
        db_ouvrage = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_up).first()
        )
        if db_ouvrage:
            for field, value in ouvrage_update.dict(exclude_unset=True).items():
                setattr(db_ouvrage, field, value)
            session.commit()
            session.refresh(db_ouvrage)
            return Ouvrage_schema.model_validate(db_ouvrage)
    raise HTTPException(
        status_code=404, detail="L'ouvrage n'a pas pu être mise à jour."
    )


##### Delete #####
@router.delete(
    "/ouvrage/{id_ouvrage_delete}",
    tags=["ouvrage"],
    summary="Effacement d'un ouvrage via son id",
    description="Saisir l'id pour le supprimer",
)
async def delete_ouvrage(id_ouvrage_delete: int):
    with Session(ENGINE) as session:
        ouvrage_db = (
            session.query(Ouvrage)
            .filter(Ouvrage.id_ouvrage == id_ouvrage_delete)
            .first()
        )
        client_comments = (
            session.query(Commentaire)
            .filter(Commentaire.id_ouvrage == id_ouvrage_delete)
            .all()
        )
        for commentaire in client_comments:
            session.delete(commentaire)
            session.commit()
        if ouvrage_db:
            session.delete(ouvrage_db)
            session.commit()
            return {"Ouvrage supprimé: ": ouvrage_db}
    raise HTTPException(status_code=404, detail="L'ouvrage n'a pas pu être supprimé.")
