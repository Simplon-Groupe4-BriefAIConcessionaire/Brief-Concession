from __init__ import db
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func


class Voitures(db.Model):
    __tablename__ = 'Voitures_occasion'
    
    id = Column(Integer,primary_key=True)
    url = Column(String(70), unique=True)
    title = Column(String(50))
    version=Column(String(60))
    prix=Column(Integer)
    annee=Column(Integer)
    kilometrage=Column(Integer)
    energie=Column(String(10))
    emissions=Column(Integer)
    transmission=Column(String(10))
    portes=Column(Integer)
    puissance=Column(Integer)
    places=Column(Integer)

    def __str__(self):
        return self.nom