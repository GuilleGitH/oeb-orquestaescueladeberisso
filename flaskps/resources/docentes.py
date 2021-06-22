from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.docente import Docente
from flaskps.models.user import User
from flask_restful import reqparse, abort, Api, Resource
import datetime
from flask_bcrypt import Bcrypt
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

put_parser = reqparse.RequestParser()
put_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='Problema con el nombre')
put_parser.add_argument('password', dest='password',location='form', required=True,help='Problema con la contraseña')
put_parser.add_argument('email', dest='email', location='form',required=True, help='Problema con el email')
put_parser.add_argument('emailPrevio', dest='emailPrevio', location='form',required=True, help='Problema con email')
put_parser.add_argument('apellido', dest='apellido', location='form',help='Problema con apellido')
put_parser.add_argument('localidad', dest='localidad', location='form',help='Problema con la localidad')
put_parser.add_argument('domicilio', dest='domicilio', location='form',help='Problema con el domicilio')
put_parser.add_argument('tipodoc', dest='tipodoc', location='form',help='Problema con el tipo')
put_parser.add_argument('telefono', dest='telefono',type=int, location='form',help='Problema con el telefono')
put_parser.add_argument('doc', dest='doc',type=int, location='form',help='Problema con el documento')
put_parser.add_argument('id', dest='id',type=int, location='form',help='Problema con el identificador')
put_parser.add_argument('fecha', dest='fecha',location='form',help='Problema con la fecha')

post_parser = reqparse.RequestParser()
post_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='Problema con el nombre')
post_parser.add_argument('password', dest='password',location='form', required=True,help='Problema con la contraseña')
post_parser.add_argument('email', dest='email', location='form',required=True, help='Problema con el email')
post_parser.add_argument('apellido', dest='apellido', location='form',help='Problema con apellido')
post_parser.add_argument('localidad', dest='localidad', location='form',help='Problema con la localidad')
post_parser.add_argument('domicilio', dest='domicilio', location='form',help='Problema con el domicilio')
post_parser.add_argument('tipodoc', dest='tipodoc', location='form',help='Problema con el tipo')
post_parser.add_argument('telefono', dest='telefono',type=int, location='form',help='Problema con el telefono')
post_parser.add_argument('doc', dest='doc',type=int, location='form',help='Problema con el documento')
post_parser.add_argument('fecha', dest='fecha',location='form',help='Problema con la fecha')

class ApiDocente(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_show' in permiso):
            abort(403)

        Docente.db = get_db()
        aux = Docente.all()
        for d in aux:
            d['fecha_nac'] = d['fecha_nac'].strftime("%d-%b-%Y")
        return aux

    def post(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_crear' in permiso):
            abort(403)

        Docente.db = get_db()
        User.db = get_db()
        params = post_parser.parse_args()
        user = User.find_by_email(params.email)
        date_time_obj = datetime.datetime.strptime(params.fecha, '%Y-%m-%d')
        if user is None:
            bcrypt = Bcrypt()
            secure_password = bcrypt.generate_password_hash(params.password)
            User.create(params.nombre, params.apellido,params.email, secure_password)
            user = User.find_by_email(params.email)
            User.rolDefault(user['id'])
            User.rolDocente(user['id'])
        else:
            flash("El mail ingresado ya esta en uso")
        Docente.create(params.apellido, params.nombre, date_time_obj, params.localidad,
                       params.domicilio, params.tipodoc, params.doc, params.telefono, params.email)
        return 201

    def put(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_update' in permiso):
            abort(403)

        Docente.db = get_db()
        User.db = get_db()
        params = put_parser.parse_args()
        user = None
        date_time_obj = datetime.datetime.strptime(params.fecha, '%Y-%m-%d')
        if not (params.emailPrevio == params.email):
            user = User.find_by_email(params.email)
        if user is None:
            User.modificar(params.apellido, params.nombre,
                           params.email, params.emailPrevio)
            Docente.modificar(params.id, params.apellido, params.nombre, date_time_obj, params.localidad,
                              params.domicilio, params.tipodoc, params.doc, params.telefono, params.email)
            return 201

class ApiDocenteSingle(Resource):
    def get(self, idD):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_show' in permiso):
            abort(403)

        Docente.db = get_db() 
        d = Docente.buscarEmail(idD)
        if (not d is None):
            d['fecha_nac'] = d['fecha_nac'].strftime("%d-%b-%Y")
            d['talleres']= Docente.talleresDe(d['id'])
            return d

    def delete(self, idD):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_borrar' in permiso):
            abort(403)

        Docente.db = get_db()
        d = Docente.buscarId(idD)
        Docente.borrarDeTalleres(idD)
        Docente.borrarDocente(idD)
        User.db=get_db()
        idUsuario=User.idDe(d['email'])
        User.borrarUsuario(d['email'])
        User.borrarDeRoles(idUsuario['id'])
        return '', 204