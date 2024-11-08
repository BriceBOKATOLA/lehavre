from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    username: str
    pwd: str

class EventSchema(BaseModel):
    title : str
    date_begin : datetime
    date_end : datetime
    place : str
    event_type : str
    organisators : str
    description : str