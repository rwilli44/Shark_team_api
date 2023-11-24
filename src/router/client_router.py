from fastapi import APIRouter
from sqlalchemy.orm import Session
from models.client import Client
from config.connexion import ENGINE

router = APIRouter()


# creation d'une route pour remplire la Bdd table client
@router.post(
    "/inscription/{nom}&{prenom}&{email}&{telephone}&{preferences}&{adresse_livraison}&{adresse_facturation}",
    tags=["client"],
)
async def ajout_client(
    nom: str,
    prenom: str,
    email: str,
    telephone: str,
    preferences: str,
    adresse_livraison: str,
    adresse_facturation: str,
):
    with Session(ENGINE) as session:
        personne = Client(
            nom_client=nom,
            prenom_client=prenom,
            email_client=email,
            telephone_client=telephone,
            preferences_client=preferences,
            adresse_livraison_client=adresse_livraison,
            adresse_facturation_client=adresse_facturation,
        )
        session.add_all([personne])
        session.commit()
    return {
        "nom :": nom,
        "Prenom :": prenom,
        "Email :": email,
        "telephone :": telephone,
        "preferences :": preferences,
        "adresse de livraison :": adresse_livraison,
        "adresse de facturation : ": adresse_facturation,
    }
