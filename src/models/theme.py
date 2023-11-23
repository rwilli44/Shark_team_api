from base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Theme(Base):
    id_theme: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom_theme: Mapped[str] = mapped_column(String(255))
