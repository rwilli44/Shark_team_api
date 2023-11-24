from pydantic import BaseModel
class Client_schema(BaseModel):

    nom_client: str 
    prenom_client: str 
    email_client: str 
    telephone_client: str 
    preferences_client: str 
    adresse_livraison_client: str 
    adresse_facturation_client: str 