# Third party imports
from pydantic import BaseModel


class Client_schema(BaseModel):
    nom_client: str
    prenom_client: str
    email_client: str
    telephone_client: str
    preferences_client: str
    adresse_livraison_client: str
    adresse_facturation_client: str

    class Config:
        orm_mode = True
        from_attributes = True


class Client_schema_optionnel(BaseModel):
    nom_client: str | None = None
    prenom_client: str | None = None
    email_client: str | None = None
    telephone_client: str | None = None
    preferences_client: str | None = None
    adresse_livraison_client: str | None = None
    adresse_facturation_client: str | None = None
