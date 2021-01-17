from main import app#, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
#import forms
from datetime import datetime
import random
import ast
import pytz

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # jugadores = Jugador.query.all()
    # form = forms.SortearForm()
    return render_template('home.html')#, jugadores=jugadores, form=form)
