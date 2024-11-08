from sqlalchemy import Column, Integer, String, DateTime
import database

class Events(database.Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date_begin = Column(DateTime)
    date_end = Column(DateTime)
    place = Column(String)
    event_type = Column(String)
    organisators = Column(String)
    description = Column(String)