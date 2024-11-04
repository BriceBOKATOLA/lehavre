import models
from app import models, schemas, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db

router = APIRouter()

class Events:
    @router.get("/events/", response_model=list[schemas.EventSchema])
    async def get_all_events(events: models.Event, db: Session = Depends(get_db)):
        events = db.query(models.Event).all()

        return [event for event in events]
    
    @router.get("/events/{event_id}", response_model = schemas.EventSchema)
    async def get_event_by_id(event_id: int, event: models.Event, db: Session = Depends(get_db)):
        event = db.query(event).filter(models.Events.id == event_id).first()
        
        return event
    
    @router.post("/events/", response_model = schemas.EventSchema)
    async def create_event(event: schemas.EventSchema, db: Session = Depends(get_db)):
        db.add(event)

        if db.commit() : 
            return True
        return False
    
    @router.put("/events/{event_id}", response_model = schemas.EventSchema)
    async def update_event(event_id: int, event: schemas.EventSchema, db: Session = Depends(get_db)):
        item = db.query(event).filter(Events.id == event_id).first()

        if item is None:
            return {"message": "Item not found"}
        
        item.title = event.title
        item.date_begin = event.date_begin
        item.date_end = event.date_end
        item.place = event.place
        item.event_type = event.event_type
        item.organisators = event.organisators
        item.description = event.description

        db.commit()

        return {"message": "Item updated successfully"}
    
    @router.delete("/events/{event_id}", response_model = schemas.EventSchema)
    async def delete_event(event_id: int, db: Session = Depends(get_db)) : 
        item = db.query(Events).filter(Events.id == event_id).first()
        
        if item is None:
            return {"message": "Item not found"}
        
        db.delete(item)
        db.commit()
        
        return {"message": "Item deleted successfully"}