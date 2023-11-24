from fastapi import APIRouter
from sqlalchemy.orm import Session
from models.client import Client
from config.connexion import ENGINE
from schema.client_schema import Client_schema
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# creation d'une route pour remplire la Bdd table client
@router.post("/inscription/")
async def ajout_client(client : Client_schema):
    with Session(ENGINE) as session:
        personne = Client(**client.dict())
        session.add_all([personne])
        session.commit()
    return {"client ajouté":personne}  

# creation d'une route pour modifier la Bdd table client
@router.patch("/modification_client/{client_id}",response_model=Client_schema)
async def modif_client(client_id : int, client : Client_schema):
    stored_client_data = client[client_id] # recuperation des données via id
    stored_client_model = Client_schema(**stored_client_data) # on transforme les données client en Client_schema
    update_data = client.dict(exclude_unset=True) # transforme données de la requète en dictionnaire
    update_client =stored_client_model.copy(update=update_data) # application de la mise à jour partielle à l'objet existant
    client[client_id] = jsonable_encoder(update_client) # mise à jour BdD avec la version mise à jour
    return update_client # retour au client de l'objet mis à jour
