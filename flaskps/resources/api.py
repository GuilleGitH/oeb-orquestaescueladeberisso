from flask import request, url_for, abort
from flaskps.db import get_db
from flaskps.models.taller import Taller
from flaskps.models.api import Api
import json

def generos():
    Api.db = get_db()
    generos = json.dumps(Api.generos())
    return generos

def escuela():
    Api.db = get_db()
    escuelas = json.dumps(Api.escuela())
    return escuelas

def barrios():
    Api.db = get_db()
    barrios = json.dumps(Api.barrio())
    return barrios

def niveles():
    Api.db = get_db()
    niveles = json.dumps(Api.nivel())
    return niveles

def talleres():
    Taller.db = get_db()
    talleres = json.dumps(Taller.buscarApi())
    return talleres

def nucleos():
    Api.db = get_db()
    nucleos = json.dumps(Api.nucleos())
    return nucleos