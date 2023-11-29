# Standard library imports
from datetime import datetime
from typing import Optional

# Third party imports
from pydantic import BaseModel


class CommentaireCreate_schema(BaseModel):
    date_publication_commentaire: datetime
    contenu_commentaire: str
    titre_commentaire: str
    id_client: int
    id_ouvrage: int


class CommentaireRequest_schema(BaseModel):
    id_commentaire: int
    date_publication_commentaire: datetime
    contenu_commentaire: str
    titre_commentaire: str
    id_client: int
    id_ouvrage: int

    class Config:
        orm_mode = True
        from_attributes = True


class CommentaireUpdate_schema(BaseModel):
    contenu_commentaire: Optional[str] = None
    titre_commentaire: Optional[str] = None
