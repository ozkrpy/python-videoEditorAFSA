from datetime import datetime
from main import db

class Jugador(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_camiseta = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.nombre}(#{self.numero_camiseta})'


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
        

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.types import Date
# from database import BASE

# class Record(BASE):
#     __tablename__='Jugador'
#     id = Column(Integer, primary_key=True, index=True)
#     nombre = Column(String)
#     numero_camiseta = Column(Integer, index=True)
#     creacion = Column(Date)

