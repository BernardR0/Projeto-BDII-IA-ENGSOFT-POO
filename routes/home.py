from flask import Blueprint, render_template
from models.models_clean import Assistido
from peewee import *

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    assistido = Assistido.select().first()  # pega o primeiro
    return render_template('index.html', assistido=assistido)
