from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, text, select
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.client import Client
from models.commentaire import Commentaire
from models.ouvrage import Ouvrage
from models.theme_ouvrage import ThemeOuvrage
from models.theme import Theme
from config.connexion import ENGINE
from router import client_router, commentaire_router

app = FastAPI()
app.include_router(client_router.router)
app.include_router(commentaire_router.router)


Base.metadata.create_all(ENGINE)
