from main import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
import forms
from datetime import datetime
import random
import ast
import pytz
from models import Jugador, Videos
from utilities import convertirHora, listarPartidos, obtenerDuracionVideo, definirParametrosDestacado, definirParametrosPartido


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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
    formulario_partido = forms.PartidoForm()
    formulario_destacado = forms.DestacadoForm()
    game = formulario_destacado.partido.data
    minuto = formulario_destacado.minuto.data
    segundo = formulario_destacado.segundo.data
    flash(definirParametrosDestacado(game, minuto, segundo))
    return render_template('home.html', 
                            formulario_partido=formulario_partido, 
                            formulario_destacado=formulario_destacado, 
                            partido=game)

@app.route("/largo", methods=["POST"])
def largo():    
    formulario_destacado = forms.DestacadoForm()
    formulario_partido = forms.PartidoForm()
    # start = formulario_partido.start_time.data
    # end = formulario_partido.end_time.data
    # print(start.hour, start.minute, start.second)
    inicio_hora = formulario_partido.inicio_hora.data
    inicio_minuto = formulario_partido.inicio_minuto.data
    inicio_segundo = formulario_partido.inicio_segundo.data
    fin_hora = formulario_partido.fin_hora.data
    fin_minuto = formulario_partido.fin_minuto.data
    fin_segundo = formulario_partido.fin_segundo.data
    # inicio = [start.hour, start.minute, start.second]
    # final = [end.hour, end.minute, end.second]
    inicio = [inicio_hora, inicio_minuto, inicio_segundo]
    final = [fin_hora, fin_minuto, fin_segundo]
    # print(inicio, final)
    flash(definirParametrosPartido(inicio, final))
    return render_template('home.html', 
                            formulario_partido=formulario_partido, 
                            formulario_destacado=formulario_destacado)



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