from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, text, select
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
password = "167943"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")

Base.metadata.create_all(engine)


#creation d'une route pour remplire la Bdd table client
@app.get("/remplissage/{nom}&{prenom}&{email}&{telephone}&{preferences}&{adresse_livraison}&{adresse_facturation}")
async def ajout_client(nom: str, prenom : str,email : str,telephone : str,preferences : str, adresse_livraison : str, adresse_facturation : str):
    with Session(engine) as session:
        personne = Client(nom_client=nom, prenom_client=prenom, email_client=email, telephone_client=telephone, preferences_client =preferences,adresse_livraison_client=adresse_livraison, adresse_facturation_client=adresse_facturation)
        session.add_all([personne])
        session.commit()
    return {"nom :" : nom,"Prenom :": prenom,"Email :":email,"telephone :":telephone,"preferences :":preferences,"adresse de livraison :":adresse_livraison,"adresse de facturation : ":adresse_facturation}
