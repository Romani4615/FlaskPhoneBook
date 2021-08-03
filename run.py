from flask import Flask, render_template
import os

app = Flask(__name__)

class Config:
    """
        setup config vars 4 flask
        ENVIRONMNENTAL VARIABLES
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favs')
def favs():
    fball = ['Buffalo Bills', 'Oakland Raiders', 'LA Rams', 'Minnesota Vikings', 'Baltimore Ravens']
    hockey = ['Buffalo Sabres', 'San Jose Sharks', 'LA Kings', 'TampaBay Lightning', 'Anaheim Ducks']
    return render_template('favs.html', title='Favorites', fball=fball, hockey=hockey)
