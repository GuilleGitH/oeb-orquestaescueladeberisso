from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify, current_app
from flaskps.db import get_db
from flask_bcrypt import Bcrypt
from flaskps.models.user import User
from flaskps.helpers.auth import habilitado, token_required
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user, current_user, LoginManager, logout_user, login_required
import jwt
from datetime import datetime, timedelta
import json

def is_correct_password(passwordHash, password):
    bcrypt = Bcrypt()
    return bcrypt.check_password_hash(passwordHash, password)

def login():
    params = request.form
    User.db = get_db()
    passwordHash = User.obtenerHash(params['email'])
    user = None
    if passwordHash:
        if is_correct_password(passwordHash['password'], params['password']):
            user = User.find_by_email_and_pass(
                params['email'], passwordHash['password'])
    if not user:
        return 'No se encontro usuario', 401
    # ahora en lugar de hacer user['email'] como ya no es un diccionario, ahora es un objeto, se usa user.propiedad: ej.  user.activo
    if user.activo == 0:
        return 'El usuario solicitado no es un usuario activo', 403
    login_user(user)
    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=59)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') }), 200


def getUserWithToken():
    header = request.headers
    user = token_required(header['Authorization'])
    if (user):
        User.db = get_db()
        u = User.find_by_email(user['email']) 
        u['updated_at'] = u['updated_at'].strftime("%d-%b-%Y")
        u['created_at'] = u['created_at'].strftime("%d-%b-%Y")
        u['roles'] = User.rolesAll(user['email'])
        if (not u['roles'] == ()):
            u['permisos'] = User.permiso(User.roles(u['email']))
        else:
            u['permisos']=[]
    else:
        abort(401)
    return json.dumps(u)

def generateToken():
    token = jwt.encode({
        'sub': current_user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=59)},
    current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })