from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.client import Client
from models.commentaire import Commentaire
from models.ouvrage import Ouvrage
from models.theme_ouvrage import ThemeOuvrage
from models.theme import Theme

app = FastAPI()

connector = "mysql+pymysql"
user = "root"
password = "password"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")

Base.metadata.create_all(engine)


# #creation d'une route pour remplire la Bdd table auteur
# @app.get("/remplissage/{nom_auteur}&{prenom_auteur}")
# async def read_item(nom_auteur: str, prenom_auteur : str):
#         pass
