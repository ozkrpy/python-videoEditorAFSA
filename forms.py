from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# class AgregarJugadorForm(FlaskForm):
#     # quotes corresponde a la etiqueta
#     nombre = StringField('Nombre', validators={DataRequired()})
#     numero = StringField('# Camiseta')
#     submit = SubmitField('Aceptar')

class PartidoForm(FlaskForm):
    submit = SubmitField('Agregar')

class DestaqueForm(FlaskForm):
    submit = SubmitField('Cortar')

# class SortearForm(FlaskForm):
#     lista = []
#     submit = SubmitField('SORTEAR')
