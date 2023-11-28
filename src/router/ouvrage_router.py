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
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_delete).first()
        )
        if ouvrage_db:
            session.delete(ouvrage_db)
            session.commit()
            return {"Ouvrage supprimé: ": ouvrage_db}

##### recherche unitaire #####
@router.get("/recherche_unitaire/{critere}/{nom}", tags=["recherche"],summary="Recherche suivant un attribut",description="Rentrer dans le critère de recherche soit auteur, soit catégorie, soit langue, soit mot clé ou titre. Ensuite  rentrer le nom que vous souhaitez afin de chercher dans la base de données")
async def get_recherche(critere : str, nom : str):
    with Session(ENGINE) as session:
        
        dic_critere = { "critere" : {"auteur": Ouvrage.auteur_ouvrage,"catégorie": Ouvrage.categorie_ouvrage,"langue":Ouvrage.langue_ouvrage,"mot clé":Ouvrage.mot_cle_ouvrage,"titre":Ouvrage.titre_ouvrage}}
        
        for cle, valeur in dic_critere["critere"].items():
            if cle == critere:
                ouvrage_db = (session.query(Ouvrage).filter(valeur.contains(nom))).all()
            break

        if ouvrage_db:
            return ouvrage_db
    raise HTTPException(status_code=404, detail="Aucun ouvrage n'a pu être trouvé.")

##### recherche double critère #####
@router.get("/recherche_double/{critere1}/{nom1}/{critere2}/{nom2}", tags=["recherche"],summary="Recherche suivant deux attributs",description="Rentrer dans les critères de recherche soit auteur, soit catégorie, soit langue, soit mot clé. Ensuite  rentrer les noms que vous souhaitez afin de chercher dans la base de données")
async def get_recherche(critere1 : str, nom1 : str,critere2 : str, nom2 : str):
    with Session(ENGINE) as session:
        
        dic_critere = { "critere" : {"auteur": Ouvrage.auteur_ouvrage,"catégorie": Ouvrage.categorie_ouvrage,"langue":Ouvrage.langue_ouvrage,"mot clé":Ouvrage.mot_cle_ouvrage,"titre":Ouvrage.titre_ouvrage}}
        
        for cle1, valeur1 in dic_critere["critere"].items():
            if cle1 == critere1:
                print("1",valeur1)
                for cle2, valeur2 in dic_critere["critere"].items():
                    print("rentré dans le 2e for")
                    if cle2 == critere2:
                        print("2",valeur1,valeur2)
                        ouvrage_db = (session.query(Ouvrage).filter(valeur1.contains(nom1)).filter(valeur2.contains(nom2))).all()
                        return ouvrage_db
                    break
            break
        if ouvrage_db:
            return ouvrage_db
    raise HTTPException(status_code=404, detail="Aucun ouvrage n'a pu être trouvé.")
