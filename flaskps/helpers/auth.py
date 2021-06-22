from flask import request, jsonify, current_app
from flaskps.db import get_db
from flaskps.models.info import Info
from flaskps.models.user import User
from functools import wraps
import jwt

def authenticated(session):
    return session.get('user')

def habilitado():
    Info.db=get_db()
    info=Info.obtener() 
    return info[0]['habilitado']

def permisos(user):
    User.db = get_db() 
    roles = User.roles(user)
    permisos = User.permiso(roles)
    list = ''
    for per in permisos:
        list+= per['nombre'] + ","
    return list

def roles(user):
    User.db = get_db()
    roles = User.rolesNom(user)
    list = ''
    for per in roles:
        list+= per['nombre'] + ","
    return list

def token_required(token):
    auth_headers = token.split()
    if len(auth_headers) != 2:
        return None
    try:
        token = auth_headers[1]
        data = jwt.decode(token, current_app.config['SECRET_KEY'])
        User.db = get_db()
        user = User.find_by_email(data['sub'])
        if not user:
            None
        return user
    except jwt.ExpiredSignatureError:
        return None # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError, Exception) as e:
        print(e)
        return None