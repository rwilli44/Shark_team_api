# Standard library imports
from datetime import date

# Third party imports
from pydantic import BaseModel


class Ouvrage_schema(BaseModel):
    titre_ouvrage: str
    auteur_ouvrage: str
    isbn_ouvrage: str
    langue_ouvrage: str
    prix_ouvrage: float
    date_parution_ouvrage: date
    categorie_ouvrage: str
    date_disponibilite_libraire_ouvrage: date
    date_disponibilite_particulier_ouvrage: date
    image_ouvrage: str
    table_des_matieres_ouvrage: str
    mot_cle_ouvrage: str
    description_ouvrage: str

    # Permet de passer facilement du modèle au schéma
    class Config:
        orm_mode = True
        from_attributes = True


class Ouvrage_schema_optionnel(BaseModel):
    titre_ouvrage: str | None = None
    auteur_ouvrage: str | None = None
    isbn_ouvrage: str | None = None
    langue_ouvrage: str | None = None
    prix_ouvrage: float | None = None
    date_parution_ouvrage: date | None = None
    categorie_ouvrage: str | None = None
    date_disponibilite_libraire_ouvrage: date | None = None
    date_disponibilite_particulier_ouvrage: date | None = None
    image_ouvrage: str | None = None
    table_des_matieres_ouvrage: str | None = None
    mot_cle_ouvrage: str | None = None
    description_ouvrage: str | None = None

    # Permet de passer facilement du modèle au schéma
    class Config:
        orm_mode = True
        from_attributes = True
