
from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()

connector = "mysql+pymysql"
user = "root"
password = "167943"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")

#creation d'une route pour remplire la Bdd table auteur
@app.get("/remplissage/{nom_auteur}&{prenom_auteur}")
async def read_item(nom_auteur: str, prenom_auteur : str):
        pass