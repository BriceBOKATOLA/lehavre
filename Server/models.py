from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    pwd = Column(String) 

class Evenement(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date_begin = Column(DateTime)
    date_end = Column(DateTime)
    place = Column(String)
    event_type = Column(String)
    organisators = Column(String)
    description = Column(String)
    