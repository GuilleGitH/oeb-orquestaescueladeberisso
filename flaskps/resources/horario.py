from flask import redirect, request, url_for, session, abort, flash
from flaskps.db import get_db
from flask_restful import reqparse, abort, Api, Resource
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.docente import Docente
from flaskps.models.asistencia import Asistencia
from flaskps.models.horarios import Horario
from flaskps.helpers.auth import authenticated, habilitado, permisos, token_required

get_parser = reqparse.RequestParser()
get_parser.add_argument('Authorization', dest='token',location='headers', required=True,help='Token missing')

post_parser = reqparse.RequestParser()
post_parser.add_argument('id_drt', dest='id_drt',location='form', required=True,help='Problema con identificador')
post_parser.add_argument('nucleo', dest='nucleo',location='form', required=True,help='Problema con el nucleo')
post_parser.add_argument('dia', dest='dia', location='form',required=True, help='Probema con el dia')
post_parser.add_argument('inicio', dest='inicio', location='form',required=True, help='Problemas con el inicio')
post_parser.add_argument('fin', dest='fin', location='form',required=True, help='Problemas con el fin')

class ApiHorario(Resource):
    def get(self, Pciclo, Ptaller, Pdocente):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_show' in permiso):
            abort(403)
        Taller.db = get_db()
        Docente.db = get_db()
        Horario.db = get_db()
        Ciclo_lectivo.db = get_db()
        docente = Docente.buscarId(Pdocente)
        taller = Taller.buscarID(Ptaller)
        ciclo = Ciclo_lectivo.buscarId(Pciclo)
        if not( ciclo is None): 
            ciclo['fecha_ini'] = ciclo['fecha_ini'].strftime("%d-%m-%Y")
            ciclo['fecha_fin'] = ciclo['fecha_fin'].strftime("%d-%m-%Y")
        idDrt = Horario.buscarIdDrt(Pdocente, Pciclo, Ptaller)
        horarios = Horario.horariosDe(idDrt['id_drt'])
        for h in horarios:
            h['inicio'] = str(h['inicio'])
            h['fin'] = str(h['fin'])
        aux = dict()	
        aux["profesor"] = docente['nombre']+' '+docente['apellido']
        aux["taller"] = taller['nombre']
        aux["fecha_ini"] = ciclo['fecha_ini']
        aux["fecha_fin"] = ciclo['fecha_fin']
        aux["year"] = ciclo['year']
        aux["semestre"] = ciclo['semestre']
        aux['horarios'] = horarios
        return aux

    def post(self, Pciclo, Ptaller, Pdocente):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_crear' in permiso):
            abort(403)
        Horario.db=get_db()
        params = post_parser.parse_args()
        Horario.create(params['id_drt'],params['nucleo'],params['dia'],params['inicio'],params['fin'])
        aux="horario registrado exitosamente."
        return aux, 201

    def delete(self,Pciclo, Ptaller, Pdocente):
        header = get_parser.parse_args()
        user=token_required(header.token)
        if not (user):
            abort(401)
        permiso = permisos(user['email'])
        if not ('administrativo_borrar' in permiso):
            abort(403)
        Horario.db=get_db()
        Horario.borrar(Pdocente)
        aux='hoario borrado exitosamente'
        return aux, 203