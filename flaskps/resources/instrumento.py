from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.instrumento import Instrumento
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

post_parser = reqparse.RequestParser()
post_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='The instrumento nombre')
post_parser.add_argument('tipo', dest='tipo',location='form', required=True,help='The instrumento tipo')
post_parser.add_argument('numeroInventario', dest='numeroInventario', required=True,location='form',help='The instrumento numeroInventario')
post_parser.add_argument('latitud', dest='latitud', location='form',required=True,help='The instrumento\'s latitud')
post_parser.add_argument('longitud', dest='longitud', location='form',required=True,help='The instrumento\'s longitud')
post_parser.add_argument('alumnoInstrumento', dest='alumnoInstrumento', required=True,location='form',help='The instrumento\'s alumnoInstrumento')

put_parser = reqparse.RequestParser()
put_parser.add_argument('instrumento_id', dest='instrumento_id', required=True, location='form',help='The instrumento\'s id')
put_parser.add_argument('nombre', dest='nombre',location='form', required=True,help='The instrumento nombre')
put_parser.add_argument('tipo', dest='tipo',location='form', required=True,help='The instrumento tipo')
put_parser.add_argument('numeroInventario', dest='numeroInventario', location='form',required=True, help='The instrumento numeroInventario')
put_parser.add_argument('latitud', dest='latitud', location='form',help='The instrumento\'s latitud')
put_parser.add_argument('longitud', dest='longitud', location='form',help='The instrumento\'s longitud')
put_parser.add_argument('alumnoInstrumento', dest='alumnoInstrumento', location='form',help='The instrumento\'s alumnoInstrumento')

class ApiInstrumento(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('instrumento_show' in permiso):
            abort(403)
        Instrumento.db = get_db()
        return Instrumento.all()

    def post(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('instrumento_crear' in permiso):
            abort(403)
        Instrumento.db = get_db()
        params = post_parser.parse_args()
        Instrumento.create(params['nombre'],params['tipo'],params['numeroInventario'], params['latitud'], params['longitud'], params['alumnoInstrumento'])
        return 'ok', 201

    def put(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('instrumento_update' in permiso):
            abort(403)
        Instrumento.db = get_db()
        params = put_parser.parse_args()
        Instrumento.modificarInstrumento(params['instrumento_id'],params['nombre'],params['tipo'],params['numeroInventario'],params['longitud'],params['latitud'],params['alumnoInstrumento'])
        #ver el tema de la imagen
        return 'ok', 201

class ApiInstrumentoSingle(Resource):
    def get(self, idI):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('instrumento_show' in permiso):
            abort(403)
        Instrumento.db = get_db()
        i = Instrumento.find_by_id(idI)
        return i

    def delete(self, idI):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('instrumento_borrar' in permiso):
            abort(403)
        Instrumento.db = get_db()
        Instrumento.borrarInstrumento(idI)
        return '', 204 