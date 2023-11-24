from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.ouvrage import Ouvrage
from datetime import date
from config.connexion import ENGINE


router = APIRouter()


class Ouvrage_schema(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage: str
    isbn_ouvrage: str
    langue_ouvrage: str | None = None
    prix_ouvrage: float
    date_parution_ouvrage: date | None = None
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: date 
    date_disponibilite_particulier_ouvrage: date
    image_ouvrage: str | None = None
    table_des_matieres_ouvrage: str | None = None
    mot_cle_ouvrage: str | None = None
    description_ouvrage: str | None = None
    commentaires: list = []
    
    # Permet de passer facilement du modèle au schéma
    class Config:
        orm_mode = True
        from_attributes = True


@router.get("/ouvrages/{id_ouvrage}")
async def get_ouvrage(id_ouvrage: int, ouvrage: Ouvrage_schema):
    results = {"id_ouvrage": id_ouvrage, "ouvrage": ouvrage}
    return results

@router.post("/ouvrage/", response_model= Ouvrage_schema)
async def create_ouvrage(ouvrage: Ouvrage_schema):
    with Session(ENGINE) as session:
        ouvrage_model = Ouvrage(**ouvrage.dict())
        session.add_all([ouvrage_model])
        session.commit()
        return Ouvrage_schema.from_orm(ouvrage_model)

@router.patch("/ouvrage/{id_ouvrage}")
async def get_ouvrage(id_ouvrage: int, ouvrage: Ouvrage_schema):
    results = {"id_ouvrage": id_ouvrage, "ouvrage": ouvrage}
    return results




""" @router.post(
    "/ouvrage/{titre}&{auteur}&{isbn}&{langue}&{prix}&{date_parution}&{categorie}&{date_dispo_librairie}&{date_dispo_particulier}&{image}&{table_des_matieres}&{mot_cle}&{description}",
    tags=["ouvrage"],
)
async def ajout_ouvrage(
    titre: str,
    auteur: str,
    isbn: str,
    langue: str,
    prix: float,
    date_parution: date,
    categorie: str,
    date_dispo_librairie: date,
    date_dispo_particulier: date,
    image: str,
    table_des_matieres: str,
    mot_cle: str,
    description: str,
):
    with Session(ENGINE) as session:
        ouvrage = Ouvrage(
            titre_ouvrage= titre, 
            auteur_ouvrage= auteur,
            isbn_ouvrage= isbn,
            langue_ouvrage= langue,
            prix_ouvrage= prix,
            date_parution_ouvrage= date_parution,
            categorie_ouvrage= categorie,
            date_disponibilite_libraire_ouvrage= date_dispo_librairie,
            date_disponibilite_particulier_ouvrage= date_dispo_particulier,
            image_ouvrage= image,
            table_des_matieres_ouvrage= table_des_matieres,
            mot_cle_ouvrage= mot_cle,
            description_ouvrage= description
        )
        session.add_all([ouvrage])
        session.commit()
    return {
        "Titre": titre,
        "Auteur": auteur,
        "ISBN": isbn,
        "Langue": langue,
        "Prix": prix,
        "Date de parution": date_parution,
        "Catégorie": categorie,
        "Date disponibilité librairie": date_dispo_librairie,
        "Date disponibilité particulier": date_dispo_particulier,
        "Image": image,
        "Table des matières": table_des_matieres,
        "Mots clés": mot_cle,
        "Description": description,
    } """