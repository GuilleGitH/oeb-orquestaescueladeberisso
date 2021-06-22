from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.estudiante import Estudiante
from datetime import datetime
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

put_parser = reqparse.RequestParser()
put_parser.add_argument('id', dest='id',location='form',required=True,help='The estudiante\'s id')
put_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='The estudiante\'s firstname')
put_parser.add_argument('apellido', dest='apellido', location='form',help='The estudiante\'s lastname')
put_parser.add_argument('localidad', dest='localidad', location='form',help='The estudiante\'s localidad')
put_parser.add_argument('domicilio', dest='domicilio', location='form',help='The estudiante\'s domicilio')
put_parser.add_argument('tipodoc', dest='tipodoc', location='form',help='The estudiante\'s tipodoc')
put_parser.add_argument('numero_doc', dest='numero_doc',type=int, location='form',help='The estudiante\'s doc')
put_parser.add_argument('numero', dest='numero',type=int, location='form',help='The estudiante\'s numero')
put_parser.add_argument('fecha_nac', dest='fecha_nac',location='form',help='The estudiante\'s fecha_nac')
put_parser.add_argument('genero', dest='genero',type=int, location='form',help='The estudiante\'s genero')
put_parser.add_argument('nivel', dest='nivel',type=int, location='form',help='The estudiante\'s nivel')
put_parser.add_argument('escuela', dest='escuela',type=int, location='form',help='The estudiante\'sescuela')
put_parser.add_argument('barrio', dest='barrio',type=int, location='form',help='The estudiante\'s barrio')
put_parser.add_argument('lugar_nac', dest='lugar_nac', location='form',help='The estudiante\'s lugar_nac')
put_parser.add_argument('responsable', dest='responsable', location='form',help='The estudiante\'s responsable')

post_parser = reqparse.RequestParser()
post_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='The estudiante\'s firstname')
post_parser.add_argument('apellido', dest='apellido', location='form', required=True,help='The estudiante\'s lastname')
post_parser.add_argument('localidad', dest='localidad', location='form', required=True,help='The estudiante\'s localidad')
post_parser.add_argument('domicilio', dest='domicilio', location='form', required=True,help='The estudiante\'s domicilio')
post_parser.add_argument('tipodoc', dest='tipodoc', location='form', required=True,help='The estudiante\'s tipodoc')
post_parser.add_argument('numero_doc', dest='numero_doc',type=int,  required=True,location='form',help='The estudiante\'s doc')
post_parser.add_argument('numero', dest='numero',type=int, location='form', required=True,help='The estudiante\'s numero')
post_parser.add_argument('fecha_nac', dest='fecha_nac',location='form', required=True,help='The estudiante\'s fecha_nac')
post_parser.add_argument('genero', dest='genero',type=int, location='form', required=True,help='The estudiante\'s genero')
post_parser.add_argument('nivel', dest='nivel',type=int, location='form', required=True,help='The estudiante\'s nivel')
post_parser.add_argument('escuela', dest='escuela',type=int, location='form', required=True,help='The estudiante\'sescuela')
post_parser.add_argument('barrio', dest='barrio',type=int, location='form', required=True,help='The estudiante\'s barrio')
post_parser.add_argument('lugar_nac', dest='lugar_nac', location='form', required=True,help='The estudiante\'s lugar_nac')
post_parser.add_argument('responsable', dest='responsable', location='form',help='The estudiante\'s responsable')

class ApiEstudiante(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('estudiante_show' in permiso):
            abort(403)
        Estudiante.db = get_db()
        aux = Estudiante.all()
        for e in aux:
            e['fecha_nac'] = e['fecha_nac'].strftime("%d-%b-%Y")
        return aux
 
    def post(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_crear' in permiso):
            abort(403)
        Estudiante.db = get_db()
        params = request.form
        Estudiante.create(params['apellido'],params['nombre'],params['fecha_nac'],params['localidad'],params['nivel'],params['domicilio'],params['genero'],params['escuela'],params['tipodoc'],params['numero_doc'],params['numero'],params['barrio'],params['lugar_nac'],params['responsable'])
        return 201
    
    def put(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('estudiante_update' in permiso):
            abort(403)
        Estudiante.db = get_db()
        params = request.form
        Estudiante.modificar(params['id'],params['apellido'],params['nombre'],params['fecha_nac'],params['localidad'],params['nivel'],params['domicilio'],params['genero'],params['escuela'],params['tipodoc'],params['numero_doc'],params['numero'],params['barrio'],params['lugar_nac'],params['responsable'])
        return 201

class ApiEstudianteSingle(Resource):
    def get(self, idE):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('estudiante_show' in permiso):
            abort(403)
        Estudiante.db = get_db()
        e = Estudiante.buscarId(idE)
        e['fecha_nac'] = e['fecha_nac'].strftime("%d-%b-%Y")
        return e

    def delete(self, idE):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('estudiante_borrar' in permiso):
            abort(403)
        Estudiante.db = get_db()
        Estudiante.borrarDeTalleres(idE)
        Estudiante.borrarEstudiante(idE)
        return '', 204