from datetime import datetime
from main import db

class Jugador(db.Model):
    __tablename__='jugador'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_camiseta = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.nombre}(#{self.numero_camiseta})[ID: {self.id}]'


class Videos(db.Model):
    __tablename__='videos'
    origen = db.Column(db.String(100), nullable=False, primary_key=True)
    inicio = db.Column(db.Integer, nullable=False, primary_key=True)
    duracion = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    id_destacado = db.Column(db.Integer, db.ForeignKey('jugador.id'), nullable=True)
    id_asistente = db.Column(db.Integer, db.ForeignKey('jugador.id'), nullable=True)
    destacado = db.relationship('Jugador',backref='destacado', foreign_keys=[id_destacado])
    asistente = db.relationship('Jugador',backref='asistente', foreign_keys=[id_asistente])

    def __repr__(self):
        #return "<entrada: {}, inicio: {}, duracion: {} - en fecha: {}>".format(self.origen, self.inicio, self.duracion, self.date)
        return f'Video: {self.origen}, tiempo: {self.inicio}, Gol: {self.destacado.nombre}, Asistencia: {self.asistente.nombre}'
