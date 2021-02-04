from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired
from utilities import listarPartidos

# class AgregarJugadorForm(FlaskForm):
#     # quotes corresponde a la etiqueta
#     nombre = StringField('Nombre', validators={DataRequired()})
#     numero = StringField('# Camiseta')
#     submit = SubmitField('Aceptar')

class PartidoForm(FlaskForm):
    inicio_hora = IntegerField('INICIO')
    inicio_minuto = IntegerField()
    inicio_segundo = IntegerField()
    fin_hora = IntegerField('FINAL')
    fin_minuto = IntegerField()
    fin_segundo = IntegerField()
    submit = SubmitField()

class DestacadoForm(FlaskForm):
    partido = SelectField('Partido', choices=listarPartidos(), validators={DataRequired()})
    minuto = StringField('Minuto')
    segundo = StringField('Segundos')
    submit = SubmitField('Cortar')

# class SortearForm(FlaskForm):
#     lista = []
#     submit = SubmitField('SORTEAR')
