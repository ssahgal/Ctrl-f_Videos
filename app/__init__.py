from flask import Flask

app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'GJ6ifT6TSU'


from app import views
from app import forms