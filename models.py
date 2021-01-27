from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base

class Record(Base):
    __tablename__='Jugador'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    numero_camiseta = Column(Integer, index=True)
    date = Column(Date)

# from datetime import datetime
# from main import db

# class Jugador(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100), nullable=False)
#     numero_camiseta = db.Column(db.Integer)
#     date = db.Column(db.Date, nullable=False)

#     def __repr__(self):
#         return f'{self.nombre}(#{self.numero_camiseta})'


