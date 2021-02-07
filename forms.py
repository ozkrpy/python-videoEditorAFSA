from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, InputRequired, ValidationError, NumberRange
from utilities import listarPartidos

# class AgregarJugadorForm(FlaskForm):
#     # quotes corresponde a la etiqueta
#     nombre = StringField('Nombre', validators={DataRequired()})
#     numero = StringField('# Camiseta')
#     submit = SubmitField('Aceptar')

def is_42(form, field):
    if field.data != 42:
        raise ValidationError('Must be 42')

class PartidoForm(FlaskForm):
    inicio_hora = IntegerField('INICIO')
    inicio_minuto = IntegerField()
    inicio_segundo = IntegerField()
    fin_hora = IntegerField('FINAL')
    fin_minuto = IntegerField()
    fin_segundo = IntegerField()
    submit = SubmitField('Partido')

class DestacadoForm(FlaskForm):
    partido = SelectField('Partido', choices=listarPartidos(), validators={DataRequired()})
    minuto = StringField('Minuto')
    segundo = StringField('Segundos')
    submit = SubmitField('Destacado')

# class SortearForm(FlaskForm):
#     lista = []
#     submit = SubmitField('SORTEAR')
