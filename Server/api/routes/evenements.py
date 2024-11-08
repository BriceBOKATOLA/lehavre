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

@router.get("/evenements/", response_model=list[schemas.Evenement])
async def get_all_equipements(db: Session = Depends(database.get_db)):
    evenements = db.query(models.Evenement).all()
    return [schemas.Evenement(**evenement.__dict__) for evenement in evenements]

#-------------------------------------------------------------------------------------------------------------------------------------------
#   get by id
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/evenement/{evenement_id}", response_model=schemas.EvenementBase)
async def get_evenement_by_id(evenement_id: int, db: Session = Depends(database.get_db)):
    evenement = db.query(models.Evenement).filter(models.Evenement.id == evenement_id).first()
    if not evenement:
        raise HTTPException(status_code=404, detail="Evenement not found")
    return schemas.EvenementBase(**evenement.__dict__)

#-------------------------------------------------------------------------------------------------------------------------------------------
#   get by dates
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.get("/weeklyEvents/}", response_model=schemas.EvenementBase)
async def get_evenement_by_id(evenement_id: int, db: Session = Depends(database.get_db)):
    weekArray = getWeek()
    evenement = db.query(models.Evenement).filter(models.Evenement.date_debut >= weekArray[0], models.Evenement.date_debut <= weekArray[1]).first()
    if not evenement:
        raise HTTPException(status_code=404, detail="Evenement not found")
    return schemas.EvenementBase(**evenement.__dict__)

def getWeek():
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return [start_of_week, end_of_week]

#-------------------------------------------------------------------------------------------------------------------------------------------
#   create
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.post("/evenement/", response_model=schemas.Evenement)
async def create_equipement(evenement: schemas.EvenementCreate, db: Session = Depends(database.get_db)):
    db_evenement = models.Evenement(**evenement.dict())
    db.add(db_evenement)
    db.commit()
    db.refresh(db_evenement)  # Recharge l'objet pour inclure les valeurs générées, comme l'ID
    return db_evenement
    
#-------------------------------------------------------------------------------------------------------------------------------------------
#   update
#-------------------------------------------------------------------------------------------------------------------------------------------
@router.put("/evenement/{evenement_id}", response_model=schemas.EvenementBase)
async def update_equipement(evenement_id: int, evenement: schemas.EvenementBase, db: Session = Depends(database.get_db)):
    db_evenement = db.query(models.Evenement).filter(models.Evenement.id == evenement_id).first()
    if not db_evenement:
        raise HTTPException(status_code=404, detail="Evenement not found")
    for key, value in evenement.dict().items():
        setattr(db_evenement, key, value)
    db.commit()
    return schemas.EvenementBase(**db_evenement.__dict__)
