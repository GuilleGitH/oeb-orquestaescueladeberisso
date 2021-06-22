from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.taller import Taller
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')
post_parser = reqparse.RequestParser()
post_parser.add_argument('año', dest='año',location='form', required=True,help='Problemas con el año')
post_parser.add_argument('numeroSemestre', dest='numeroSemestre', location='form', required=True,help='problemas con el semestre')
post_parser.add_argument('inicioSemestre', dest='inicioSemestre', location='form', required=True,help='Problemas con el inicio')
post_parser.add_argument('finSemestre', dest='finSemestre', location='form', required=True,help='Problemas con el fin')

class ApiCiclo_lectivo(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)

        Ciclo_lectivo.db = get_db()
        aux = Ciclo_lectivo.all()
        for c in aux:
            c['fecha_ini'] = c['fecha_ini'].strftime("%d-%b-%Y")
            c['fecha_fin'] = c['fecha_fin'].strftime("%d-%b-%Y")
            Taller.db = get_db()
            c['talleres'] = Taller.talleresDeCiclo(c['id'])
        return aux

    def post(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_crear' in permiso):
            abort(403)
        Ciclo_lectivo.db = get_db()
        params = post_parser.parse_args()
        ciclo_id=Ciclo_lectivo.buscar(params['año'], params['numeroSemestre'])
        if (ciclo_id is None):
            Ciclo_lectivo.create(params['inicioSemestre'],params['finSemestre'],params['numeroSemestre'],params['año'])
            aux="Ciclo creado exitosamente."
            return aux, 201
        else:
            aux="ciclo lectivo ya existe."
            return aux, 409
        
class ApiCiclo_lectivoSingle(Resource):
    def get(self, idC):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)
        Ciclo_lectivo.db = get_db()
        c = Ciclo_lectivo.buscarId(idC)
        if not( c is None): 
            c['fecha_ini'] = c['fecha_ini'].strftime("%d-%b-%Y")
            c['fecha_fin'] = c['fecha_fin'].strftime("%d-%b-%Y")
            Taller.db = get_db()
            c['talleres'] = Taller.talleresDeCiclo(c['id'])
        return c