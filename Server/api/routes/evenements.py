from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import database
from datetime import datetime, timedelta
import models, schemas, database

router = APIRouter()

#-------------------------------------------------------------------------------------------------------------------------------------------
#   get all
#-------------------------------------------------------------------------------------------------------------------------------------------

@router.get("/events/", response_model=list[schemas.Evenement])
async def get_all(db: Session = Depends(database.get_db)):
    evenements = db.query(models.Events).all()
    return [schemas.Evenement(**evenement.__dict__) for evenement in evenements]

#-------------------------------------------------------------------------------------------------------------------------------------------
#   get by id
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/events/{evenement_id}", response_model=schemas.EvenementBase)
async def get_evenement_by_id(evenement_id: int, db: Session = Depends(database.get_db)):
    evenement = db.query(models.Events).filter(models.Events.id == evenement_id).first()
    if not evenement:
        raise HTTPException(status_code=404, detail="Evenement not found")
    return schemas.EvenementBase(**evenement.__dict__)

#-------------------------------------------------------------------------------------------------------------------------------------------
#   get by dates
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/weeklyEvents/}", response_model=list[schemas.Evenement])
async def get_evenement_by_id(db: Session = Depends(database.get_db)):
    weekArray = getWeek()
    evenements = db.query(models.Events).filter(models.Events.date_begin >= weekArray[0], models.Events.date_begin <= weekArray[1]).all()
    if not evenements:
        raise HTTPException(status_code=404, detail="Evenement not found")
    return [schemas.Evenement(**evenement.__dict__) for evenement in evenements]

def getWeek():
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return [start_of_week, end_of_week]

#-------------------------------------------------------------------------------------------------------------------------------------------
#   create
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.post("/events/", response_model=schemas.Evenement)
async def create_equipement(evenement: schemas.EvenementCreate, db: Session = Depends(database.get_db)):
    db_evenement = models.Events(**evenement.dict())
    db.add(db_evenement)
    db.commit()
    db.refresh(db_evenement)  # Recharge l'objet pour inclure les valeurs générées, comme l'ID
    return db_evenement
    
#-------------------------------------------------------------------------------------------------------------------------------------------
#   update
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.put("/events/{evenement_id}", response_model=schemas.EvenementBase)
async def update_equipement(evenement_id: int, evenement: schemas.EvenementBase, db: Session = Depends(database.get_db)):
    db_evenement = db.query(models.Events).filter(models.Events.id == evenement_id).first()
    if not db_evenement:
        raise HTTPException(status_code=404, detail="Evenement not found")
    for key, value in evenement.dict().items():
        setattr(db_evenement, key, value)
    db.commit()
    return schemas.EvenementBase(**db_evenement.__dict__)
