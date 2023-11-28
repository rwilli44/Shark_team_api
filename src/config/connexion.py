# Standard library imports
import os

# Third party imports
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Load environment variables from .env file
load_dotenv()

# Variables needed to create the DB connection through
# the engine
connector = "mysql+pymysql"
user = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = "localhost"
database = "test"

# Creates an Engine which is used throughout the app to connect to the DB
ENGINE = create_engine(f"{connector}://{user}:{password}@{host}/{database}")


# Function which may be called from
# elsewhere in the app to create a session
async def get_db() -> Session:
    session = Session(ENGINE)
    try:
        yield session
    finally:
        session.close()
