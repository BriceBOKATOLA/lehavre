from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr

class EvenementBase(BaseModel):
    titre: str
    date_debut: datetime
    date_fin: datetime
    lieu: str
    type_evenement: str
    organisateurs: str

class EvenementCreate(EvenementBase):
    pass

class Evenement(EvenementBase):
    id: int

