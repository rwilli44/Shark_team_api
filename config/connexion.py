from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

# connexion à la base de donnée
connector = "mysql+pymysql"
user = "root"
password = "root"
host = "localhost"
database = "librairie"

engine = create_engine(f"{connector}://{user}:{password}@{host}/{database}")
conn = engine.connect()

# créer les tables
class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)