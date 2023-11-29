# Third party imports
from sqlalchemy.orm import DeclarativeBase


# créer les tables
class Base(DeclarativeBase):
    """Classe nécessaire pour assurer que toutes les classe qui
    sont modèles de tables hérite de DeclarativeBase ce qui
    est nécessaire pour certains foncitonnalités comme la
    création automatique des tables dans la base de données"""

    pass
