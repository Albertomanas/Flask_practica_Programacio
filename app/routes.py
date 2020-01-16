from app import app
from flask import render_template


@app.route('/')
@app.route('/index/')
def index():
    hola_mundo = "HOLA, OK BOOMER, MUNDO"
    return render_template('index.html', hola_mundo=hola_mundo)
