# [START gae_python38_app]
from flask import Flask, _app_ctx_stack, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import os 
from pathlib import Path
from parametricos import PATHAFSA, PATHGOLES

def verificarDirectorios():
    Path(PATHAFSA).mkdir(parents=True, exist_ok=True)
    Path(PATHGOLES).mkdir(parents=True, exist_ok=True)


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data.db"))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'textoDeSeguridad'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from routes import *   

firstime = True 

if __name__ == "__main__":
    if firstime:
        verificarDirectorios()
        db.create_all()
        firstime = False
    app.run(debug=True)
# [END gae_python38_app]