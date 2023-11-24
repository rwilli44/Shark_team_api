from pydantic import BaseModel
from datetime import datetime


class Commentaire_schema(BaseModel):
    date_publication_commentaire: datetime
    contenu_commentaire: str
    titre_commentaire: str
    id_client: int
    id_ouvrage: int
