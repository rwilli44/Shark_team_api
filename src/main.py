# Third party imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData, Table, text, select
from sqlalchemy.orm import Session, sessionmaker

# Local imports
from config.connexion import ENGINE
from models.base import Base
from models.client import Client
from models.commentaire import Commentaire
from models.ouvrage import Ouvrage
from models.theme import Theme
from models.theme_ouvrage import ThemeOuvrage
from router import (
    client_router,
    commentaire_router,
    ouvrage_router,
    theme_router,
)

# Créer l'API
app = FastAPI()

# Ajouter chaque router à l'API
app.include_router(client_router.router)
app.include_router(commentaire_router.router)
app.include_router(ouvrage_router.router)
app.include_router(commentaire_router.router)
app.include_router(theme_router.router)

# Créer les tables de BDD à partir des modèles importés
Base.metadata.create_all(ENGINE)


# Cette partie est nécessaire pour tester le front en local.
# Elle permet au serveur lancé par Go Live sur la porte 5500
# de faire des requêtes sans provoquer une erreur CORS
origins = ["http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
