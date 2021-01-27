from main import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request
# import forms
from datetime import datetime
import random
import ast
import pytz
from utilities import convertirHora


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # return render_template('home.html')
    return render_template('home.html')
