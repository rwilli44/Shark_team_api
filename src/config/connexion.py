import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

connector = "mysql+pymysql"
user = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = "localhost"
database = "librairie"

ENGINE = create_engine(f"{connector}://{user}:{password}@{host}/{database}")


async def get_db() -> Session:
    session = Session(ENGINE)
    try:
        yield session
    finally:
        session.close()
