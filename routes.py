from main import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
import forms
from datetime import datetime
import random
import ast
import pytz
from models import Jugador, Book
from utilities import convertirHora, listarPartidos, obtenerDuracionVideo, definirParametrosDestacado


@app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
def home():
    formulario_partido = forms.PartidoForm()
    formulario_destacado = forms.DestacadoForm()
    if request.method == 'GET':
        formulario_destacado.partido.default = '0'
        formulario_destacado.process()
    return render_template('home.html', 
                            formulario_partido=formulario_partido, 
                            formulario_destacado=formulario_destacado)

@app.route("/corto", methods=["POST"])
def corto():
    print ('entro a corto')
    formulario_partido = forms.PartidoForm()
    formulario_destacado = forms.DestacadoForm()
    game = formulario_destacado.partido.data
    minuto = formulario_destacado.minuto.data
    segundo = formulario_destacado.segundo.data
    definirParametrosDestacado(game, minuto, segundo)
    return render_template('home.html', 
                            formulario_partido=formulario_partido, 
                            formulario_destacado=formulario_destacado, 
                            partido=game)

@app.route("/largo", methods=["POST"])
def largo():
    print ('entro a largo')
    form = forms.PartidoForm()
    # if form.validate_on_submit():
    #     print(form.partido.data)
    return redirect("/")



 # if request.method == 'GET':
    #     formulario_destacado.partido.default = 'Partido3'
    #     form.process()
    # elif form.validate_on_submit():
    #     print('validado')
    # if request.form:
    #     print(request.form.get("partido"))
    #     book = Book(title=request.form.get("title"))
    #     db.session.add(book)
    #     db.session.commit()
    # books = Book.query.all()