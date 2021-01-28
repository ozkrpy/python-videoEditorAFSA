from main import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
import forms
from datetime import datetime
import random
import ast
import pytz
from models import Jugador
from utilities import convertirHora


@app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
def home():
    partido = forms.PartidoForm()
    destacado = forms.DestaqueForm()
    if request.form:
        print(request.form)
    return render_template('home.html', partido=partido, destacado=destacado)
