from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr

class EvenementBase(BaseModel):
    title : str
    date_begin : datetime
    date_end : datetime
    place : str
    event_type : str
    organisators : str
    description : str

class EvenementCreate(EvenementBase):
    pass

class Evenement(EvenementBase):
    id: int

