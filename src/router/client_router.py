from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.client import Client
from config.connexion import ENGINE
from schema.client_schema import Client_schema, Client_schema_optionnel
from fastapi.encoders import jsonable_encoder
from config.connexion import get_db
from models.commentaire import Commentaire

router = APIRouter()


# creation d'une route pour remplire la Bdd table client
@router.post(
    "/inscription/",
    status_code=201,
    tags=["Client"],
    summary="Inscription dans la base de données",
    description="Remplire le nom_client, prenom_client, email_client,telephone_client, preferences_client, adresse_livraison_client, adresse_facturation_client",
)
async def ajout_client(client: Client_schema):
    try:
        with Session(ENGINE) as session:
            personne = Client(**client.dict())
            session.add_all([personne])
            session.commit()
            return Client_schema.from_orm(personne)
    except Exception as e:
        raise HTTPException(
            status_code=404, detail=f"Le client n'a pas pu être ajouté : '{str(e)}'."
        )


# creation d'une route pour avoir information client de la Bdd table client
@router.get(
    "/information_client/{id}",
    tags=["Client"],
    summary="Affichage des informations relatives à un client via son id",
    description="Rentrer l'identité du client pour voir ses informations ",
)
async def information_client(id: int):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            return {"info client": client_db}
    raise HTTPException(
        status_code=404, detail="Aucune information disponible sur ce client."
    )


# creation d'une route pour effacer la Bdd table client
@router.delete(
    "/suppression_client/{id}",
    tags=["Client"],
    summary="Suppression d'un client dans la base de données via son id",
    description="Rentrer l'identité du client et appuyer sur supprimer",
)
async def suppression_client(id: int):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            client_comments = (
                session.query(Commentaire).filter(Commentaire.id_client == id).all()
            )
            for commentaire in client_comments:
                print(commentaire)
                session.delete(commentaire)
                session.commit()
            session.delete(client_db)
            session.commit()
            return {"personne supprimée": client_db}
    raise HTTPException(status_code=404, detail="Suppression client impossible.")


# creation d'une route pour modifier la Bdd table client
@router.patch(
    "/modification_client/{id}",
    response_model=Client_schema,
    tags=["Client"],
    summary="Modification d'un client dans la base de données via son id",
    description="Rentrer l'identité du client et modifier seulement les attribus nécessaires",
)
async def modif_client(id: int, client_update: Client_schema_optionnel):
    with Session(ENGINE) as session:
        client_db = session.query(Client).filter(Client.id_client == id).first()
        if client_db:
            for cle, valeur in client_update.dict(exclude_unset=True).items():
                setattr(client_db, cle, valeur)
            session.commit()
            session.refresh(client_db)
            return Client_schema.from_orm(client_db)
    raise HTTPException(
        status_code=404, detail="La mise à jour du client n'a pu être réalisée."
    )


"""
Vu avec Robin, ne fonctionne pas : pbe de dict sur stored_client_model
Code Robin en deuxième partie, non utilisé, on est passé en query

# creation d'une route pour modifier la Bdd table client
@router.patch("/modification/{id}",response_model=Client_schema)
async def modif_client(id : int, client : Client_schema_optionnel, bdd : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id)
    stored_client_data = bdd.scalars(stmt).one() # recuperation des données via id
    stored_client_model = Client(**stored_client_data.dict()) # on transforme les données client en Client pour exploitation 
    update_data = client.dict(exclude_unset=True) # transforme données de la requète en dictionnaire
    update_client =stored_client_model.copy(update=update_data) # application de la mise à jour partielle à l'objet existant
    Session.commit(update_client) # on commit pour "fermer l'enveloppe"
    Session.refresh(update_client) # mise à jour BdD avec la version mise à jour
    return update_client # retour au client de l'objet mis à jour

@router.patch("/{id_client}", response_model=Client_schema, status_code=200)
def update_client(id_client: int, client: Client_schema_optionnel, db : Session = Depends(get_db)):
    stmt = select(Client).where(Client.id_client == id_client)
    result = db.scalars(stmt).first()
    for key, value in client.dict().items():
        setattr(result, key, value)
    db.commit()
    return result
"""
