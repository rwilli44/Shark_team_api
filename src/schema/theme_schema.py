from pydantic import BaseModel


class Theme_CreateUpdate_Schema(BaseModel):
    nom_theme: str


class Theme_Read_Schema(BaseModel):
    id_theme: int
    nom_theme: str

    class Config:
        orm_mode = True
        from_attributes = True
