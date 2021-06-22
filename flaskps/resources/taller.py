from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource 
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

post_parser = reqparse.RequestParser()
post_parser.add_argument('tallerId', dest='tallerId',location='form', required=True,help='Problemas con el identificador')
post_parser.add_argument('añoTaller', dest='añoTaller',location='form', required=True,help='Problemas con el año')
post_parser.add_argument('semestreTaller', dest='semestreTaller', location='form',required=True, help='Problemas con el semestre')

class ApiTaller(Resource):
    def get(self):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)
        Taller.db = get_db()
        return Taller.all()

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
        ciclo_id=Ciclo_lectivo.buscar(params['añoTaller'], params['semestreTaller'])
        if (ciclo_id is None):
            flash("el Ciclo selecionado no existe.")
        else:
            rel=Ciclo_lectivo.buscarTallerCiclo(ciclo_id['id'], params['tallerId'])
            if (not rel is None):
                flash("Taller ya resgistrado en esete ciclo lectivo.")
            else:
                Ciclo_lectivo.agregarTaller(params['tallerId'], ciclo_id['id'])
                flash("Taller agregado exitosamente.")
        return '', 201
 
class ApiTallerSingle(Resource):
    def get(self, ciclo, idT):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)
        Taller.db = get_db()
        t = Taller.buscarID(idT)
        Taller.db = get_db()
        docentes = Taller.buscarDocentes(idT, ciclo)
        estudiantes = Taller.buscarEstudiantes(idT, ciclo)
        docentesNo = Taller.buscarDocentesNo(idT, ciclo)
        estudiantesNo = Taller.buscarEstudiantesNo(idT, ciclo)
        t['docentes'] = docentes
        t['estudiantes'] = estudiantes
        t['docentesNo'] = docentesNo
        t['estudiantesNo'] = estudiantesNo
        return t

class ApiTallerDocente(Resource):
    def post(self, ciclo, taller, docente):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_crear' in permiso):
            abort(403)
        Taller.db = get_db()
        Taller.agregarDocenteATaller(docente,ciclo,taller)
        aux="Docente agregado exitosamente."
        return aux, 201 
    
    def delete(self, ciclo, taller, docente):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_borrar' in permiso):
            abort(403)
        Taller.db = get_db()
        Taller.borrarDocenteDeTaller(docente,ciclo,taller)
        aux="Docente eliminado exitosamente."
        return aux, 204

class ApiTallerEstudiante(Resource):
    def post(self, ciclo, taller, estudiante):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_crear' in permiso):
            abort(403)
        Taller.db = get_db()
        Taller.AgregarEstudianteATaller(estudiante,ciclo,taller)
        aux="estudiante agregado exitosamente."
        return aux, 201
    
    def delete(self, ciclo, taller, estudiante):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_borrar' in permiso):
            abort(403)
        Taller.db = get_db()
        Taller.borrarEstudianteDeTaller(estudiante,ciclo,taller)
        aux="estudiante eliminado exitosamente."
        return aux, 204