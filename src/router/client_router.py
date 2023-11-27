
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
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

def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
        
#modification paramètre client
@router.get("/modification/{id}")
async def extraction_client(id : int, bdd : Session = Depends(get_db)):
    stmt = select(Client).where(id == Client.id_client)
    json_result = bdd.scalars(stmt).one()
    return json_result


# creation d'une route pour modifier la Bdd table client
@router.patch("/modification/{id}",response_model=Client_schema)
async def modif_client(id : int, client : Client_schema, bdd : Session = Depends(get_db)):
    stored_client_data = extraction_client(id,bdd) # recuperation des données via id
    stored_client_model = Client_schema(**stored_client_data) # on transforme les données client en Client_schema pour exploitation 
    update_data = client.dict(exclude_unset=True) # transforme données de la requète en dictionnaire
    update_client =stored_client_model.copy(update=update_data) # application de la mise à jour partielle à l'objet existant
    Session.commit(update_client) # on commit pour "fermer l'enveloppe"
    Session.refresh(update_client) # mise à jour BdD avec la version mise à jour
    return update_client # retour au client de l'objet mis à jour