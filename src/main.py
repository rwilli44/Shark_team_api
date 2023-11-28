# Third party imports
from fastapi import FastAPI
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
