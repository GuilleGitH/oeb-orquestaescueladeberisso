from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.info import Info
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

put_parser = reqparse.RequestParser()
put_parser.add_argument('titulo', dest='titulo',location='form', required=True,help='Problemas con el titulo')
put_parser.add_argument('descripcion', dest='descripcion',location='form', required=True,help='Problemas con la dscripcion')
put_parser.add_argument('contacto', dest='contacto', location='form',required=True, help='Problemas con el email')
put_parser.add_argument('cantidadfilas', dest='cantidadfilas', location='form',required=True, help='Problemas con las filas')
put_parser.add_argument('habilitado', dest='habilitado', location='form',help='Problemas con la habilitacion')

class ApiInfo(Resource):
    def get(self):
        Info.db = get_db()
        info=Info.obtener()
        return info

    def put(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('configuracion_configurar' in permiso):
            abort(403)
        params = put_parser.parse_args()
        Info.cambiarInfo(params['titulo'],params['descripcion'],params['contacto'],params['cantidadfilas'], params['habilitado'])
        aux='sitio actualizado correctamente'
        return aux, 201