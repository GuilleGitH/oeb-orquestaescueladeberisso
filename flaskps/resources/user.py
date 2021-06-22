from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.user import User
from flaskps.models.docente import Docente
from datetime import datetime
from flask_bcrypt import Bcrypt
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

post_parser = reqparse.RequestParser()
post_parser.add_argument('fullname', dest='fullname',location='form', required=True,help='The user\'s firstname')
post_parser.add_argument('password', dest='password',location='form', required=True,help='The user\'s firstname')
post_parser.add_argument('email', dest='email', location='form',required=True, help='The user\'s email')
post_parser.add_argument('lastname', dest='lastname', location='form',help='The user\'s lastname')

contra_parser = reqparse.RequestParser()
contra_parser.add_argument('password', dest='password',location='form', required=True, help='The user\'s Contra')

put_parser = reqparse.RequestParser()
put_parser.add_argument('fullname', dest='fullname',location='form', required=True,help='The user\'s firstname')
put_parser.add_argument('email', dest='email', location='form',required=True, help='The user\'s email')
put_parser.add_argument('emailPrevio', dest='emailPrevio', location='form',required=True, help='The user\'s email')
put_parser.add_argument('lastname', dest='lastname', location='form',help='The user\'s lastname')
put_parser.add_argument('inadministrador', dest='inadministrador', location='form',help='The user\'s inadministrador')
put_parser.add_argument('inpreceptor', dest='inpreceptor', location='form',help='The user\'s inpreceptor')

class ApiUser(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_leer' in permiso):
            abort(403)
        User.db = get_db()
        aux = User.all()
        for u in aux:
            u['updated_at'] = u['updated_at'].strftime("%d-%b-%Y")
            u['created_at'] = u['created_at'].strftime("%d-%b-%Y")
            u['roles'] = User.rolesAll(u['email'])
            if (not u['roles'] == ()):
                u['permisos'] = User.permiso(User.roles(u['email']))
            else:
                u['permisos']=[]
        return aux
 
    def post(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_crear' in permiso):
            abort(403)
        User.db = get_db()
        params = post_parser.parse_args()
        user = User.find_by_email(params['email'])
        if user is None:
            bcrypt = Bcrypt()
            secure_password= bcrypt.generate_password_hash(params['password'])
            User.create(params['fullname'],params['lastname'],params['email'],secure_password)
            user = User.find_by_email(params['email'])
            User.rolDefault(user['id'])
            flash('usuario registrado exitosamente')
            return 201
    
    def put(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_modificar' in permiso):
            abort(403)
        User.db = get_db()
        Docente.db = get_db()
        params = put_parser.parse_args()
        user = None
        if not (params['emailPrevio'] == params['email']):
            user = User.find_by_email(params['email'])
        if user is None:
            Docente.modificarUser(params['emailPrevio'], params['fullname'], params['lastname'], params['email'])
            User.modificar(params['fullname'], params['lastname'], params['email'], params['emailPrevio'])
            agregar = []
            if params['inadministrador'] == '1':
                agregar.append('1')
            if params['inpreceptor'] == '1':
                agregar.append('2')
            user = User.find_by_email(str(params['email']))
            User.actualizarPermisos(user, agregar)
            return 201
        else:
            return 'El mail ingresado ya esta en uso', 200

class ApiUserSingle(Resource):
    def get(self, email):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_leer' in permiso):
            abort(403)
        User.db = get_db()
        u = User.find_by_email(email)
        u['updated_at'] = u['updated_at'].strftime("%d-%b-%Y")
        u['created_at'] = u['created_at'].strftime("%d-%b-%Y")
        u['roles'] = User.rolesAll(email)
        if (not u['roles'] == ()):
            u['permisos'] = User.permiso(User.roles(email))
        else:
            u['permisos']=[]
        return u

    def delete(self, email):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_borrar' in permiso):
            abort(403)
        User.db=get_db()
        idUsuario=User.idDe(email)
        User.borrarUsuario(email) 
        User.borrarDeRoles(idUsuario['id'])
        return '', 204
        
    def put(self, email):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        User.db = get_db()
        Docente.db = get_db()
        params = contra_parser.parse_args()
        bcrypt = Bcrypt()
        secure_password= bcrypt.generate_password_hash(params['password'])
        User.cambiarContraseña(user['email'], secure_password)
        return 201
        
    
class ApiUserActivation(Resource):
    def put(self, idU, activar):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('usuario_modificar' in permiso):
            abort(403)
        User.db = get_db()
        if (activar == "activar"):
            User.activar(idU)
        else:
            User.desactivar(idU)
        return 'ok'

class ApiImg(Resource):
    def get(self, folder, resource):
        return redirect(url_for('static', filename=folder+'/'+resource))