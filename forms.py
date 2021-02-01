from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from utilities import listarPartidos

# class AgregarJugadorForm(FlaskForm):
#     # quotes corresponde a la etiqueta
#     nombre = StringField('Nombre', validators={DataRequired()})
#     numero = StringField('# Camiseta')
#     submit = SubmitField('Aceptar')

class PartidoForm(FlaskForm):
    inicio_hora = StringField('INICIO')
    inicio_minuto = StringField()
    inicio_segundo = StringField()
    fin_hora = StringField()
    fin_minuto = StringField('FINAL')
    fin_segundo = StringField()
    submit = SubmitField()

class DestacadoForm(FlaskForm):
    partido = SelectField('Partido', choices=listarPartidos(), validators={DataRequired()})
    minuto = StringField('Minuto')
    segundo = StringField('Segundos')
    submit = SubmitField('Cortar')

# class SortearForm(FlaskForm):
#     lista = []
#     submit = SubmitField('SORTEAR')
