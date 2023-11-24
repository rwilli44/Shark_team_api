from pydantic import BaseModel


class Theme(BaseModel):
    nom_theme: str
    ouvrages: list = []

    class Config:
        orm_mode = True
        from_attributes = True
