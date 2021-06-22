from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.asistencia import Asistencia
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

post_parser = reqparse.RequestParser()
post_parser.add_argument('id_drt', dest='id_drt',location='form', required=True,help='Problemas con el id')
post_parser.add_argument('fecha', dest='fecha',location='form', required=True,help='Problemas con la fecha')
post_parser.add_argument('estado', dest='estado', location='form',required=True, help='Problemas con el estado')
post_parser.add_argument('estudianteId', dest='estudianteId', location='form',required=True, help='Problemas con el alumno')

class ApiAsistencia(Resource):
    def get(self, Pciclo, Ptaller, Pfecha):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)
        Asistencia.db = get_db()
        return Asistencia.buscarEstudiantesAsist(Ptaller,Pciclo,Pfecha)
     
    def post(self, Pciclo, Ptaller, Pfecha):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('docente_crear' in permiso):
            abort(403)
        params = post_parser.parse_args()
        Asistencia.db = get_db()
        asis=Asistencia.buscarAsistencia(params['id_drt'], params['fecha'], params['estudianteId'])
        if (asis is None):
            Asistencia.create(params['id_drt'], params['fecha'], params['estado'], params['estudianteId'])
        else:
            Asistencia.modificar(params['id_drt'], params['fecha'], params['estado'], params['estudianteId'])
        return 'ok', 201