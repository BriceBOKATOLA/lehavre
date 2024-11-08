from sqlalchemy import Column, Integer, String, DateTime
import database

class Evenement(database.Base):
    __tablename__ = "evenement"
    
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    lieu = Column(String, index=True)
    type_evenement = Column(String, index=True)
    organisateurs = Column(String, index=True)