from fastapi import APIRouter, HTTPException
from schema.ouvrage_schema import Ouvrage_schema, Ouvrage_schema_optionnel
from sqlalchemy.orm import Session
from models.ouvrage import Ouvrage
from config.connexion import ENGINE


router = APIRouter()


##### Read #####
@router.get("/ouvrage/{id_ouvrage_get}", tags=["ouvrage"])
async def get_ouvrage(
    id_ouvrage_get: int,
):
    with Session(ENGINE) as session:
        ouvrage_db = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_get).first()
        )
        if ouvrage_db:
            return ouvrage_db
    raise HTTPException(status_code=404, detail="L'ouvrage n'a pas pu être retrouvé.")


##### Create #####
@router.post(
    "/ouvrage/",
    response_model=Ouvrage_schema,
    tags=["ouvrage"],
    summary="Créer un ouvrage",
)
async def create_ouvrage(ouvrage: Ouvrage_schema):
    with Session(ENGINE) as session:
        ouvrage_model = Ouvrage(**ouvrage.dict())
        session.add_all([ouvrage_model])
        session.commit()
        return Ouvrage_schema.from_orm(ouvrage_model)


##### Update #####
@router.patch("/ouvrage/{id_ouvrage_up}", response_model=Ouvrage_schema, tags=["ouvrage"])
async def update_ouvrage(id_ouvrage_up: int, ouvrage: Ouvrage_schema_optionnel):
    with Session(ENGINE) as session:
        db_ouvrage = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_up).first()
        )
        if db_ouvrage:
            for key, value in ouvrage.dict(exclude_unset=True).items():
                setattr(db_ouvrage, key, value)
            session.commit()
            session.refresh(db_ouvrage)
        return Ouvrage_schema.from_orm(db_ouvrage)


##### Delete #####
@router.delete("/ouvrage/{id_ouvrage_delete}", tags=["ouvrage"])
async def delete_ouvrage(id_ouvrage_delete: int):
    with Session(ENGINE) as session:
        ouvrage_db = (
            session.query(Ouvrage).filter(Ouvrage.id_ouvrage == id_ouvrage_delete).first()
        )
        if ouvrage_db:
            session.delete(ouvrage_db)
            session.commit()
            return {"Ouvrage supprimé: ": ouvrage_db}
