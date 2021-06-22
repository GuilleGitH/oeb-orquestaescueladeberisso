import os
from os import path
from flask import Flask, render_template, request, g, url_for, session, redirect, abort, flash, send_from_directory
from flask_session import Session
from flaskps.config import Config
from werkzeug.utils import secure_filename
from flaskps.db import get_db
from flaskps.resources import auth
from flaskps.resources.docentes import ApiDocente, ApiDocenteSingle
from flaskps.resources.instrumento import ApiInstrumento, ApiInstrumentoSingle
from flaskps.resources.ciclo_lectivo import ApiCiclo_lectivo, ApiCiclo_lectivoSingle
from flaskps.resources.info import ApiInfo
from flaskps.resources.estudiantes import ApiEstudiante, ApiEstudianteSingle
from flaskps.resources.horario import ApiHorario
from flaskps.resources.asistencia import ApiAsistencia
from flaskps.resources.info import ApiInfo
from flaskps.resources.taller import ApiTaller, ApiTallerSingle, ApiTallerDocente, ApiTallerEstudiante
from flaskps.resources.user import ApiUser, ApiUserSingle, ApiUserActivation, ApiImg
from flaskps.resources import api
from flaskps.models.info import Info
from flaskps.models.user import User
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user, current_user, LoginManager, logout_user, login_required

UPLOAD_FOLDER = os.path.abspath('flaskps/static/uploads')
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
ALLOWED_EXTENSIONS = set(['jpg'])

# Configuración inicial de la app
app = Flask(__name__)
CORS(app)
API = Api(app)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Oauth Variables
app.config["GOOGLE_OAUTH_CLIENT_ID"] = '288399383877-7ksdj7vkm84shv92m79ic3s5d9d6di7t.apps.googleusercontent.com'
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = 'BUGHEkSea5qL0tqn11pLTmzH'
# Configuracion de Oauth
blueprint = make_google_blueprint(
    scope=["profile", "email", "openid"], offline=True, reprompt_consent=True, redirect_to='index'
)
app.register_blueprint(blueprint, url_prefix="/login_google")
# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
# Server Side session}
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Rutas Generales


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/cargarArchivo", methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        print('No selected file')
        return 'no' , 400
    if file:
        print(file)
        filename = request.form['n_inventario'] + ".jpg"
        file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Imagen cargada correctamente', 200


@app.route("/modificarArchivo", methods=['POST'])
def mod_file():
    file = request.files['file']
    if not file:
        print('No selected file')
        return 'no' , 400
    if file:
        print(file)
        filename = request.form['n_inventario'] + ".jpg"
        file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Imagen cargada correctamente', 200


@login_manager.user_loader
def load_user(user_id):
    User.db = get_db()
    return User.porID(user_id)


@app.route("/login_google")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v3/userinfo")
    assert resp.ok
    User.db = get_db()
    user = User.porEmail(resp.json()['email'])
    login_user(user)
    return redirect(url_for('hello'))

@app.route("/oauthloged")
def oauthlog():
    if current_user.is_authenticated:
        return auth.generateToken()
    return 'User not logged in via oauth', 204

@app.route("/logout", methods=['POST'])
def logout():
    if google.authorized:
        resp = google.post('https://oauth2.googleapis.com/revoke',
        params={'token': app.blueprints['google'].token["access_token"]},
        headers = {'content-type': 'application/x-www-form-urlencoded'})
        if resp.ok:
            del app.blueprints['google'].token
    session.clear()
    logout_user()
    return 'ok', 200


# Rutas api
app.add_url_rule("/apigeneros", 'apigeneros', api.generos)
app.add_url_rule("/apiescuelas", 'apiescuelas', api.escuela)
app.add_url_rule("/apibarrios", 'apibarrios', api.barrios)
app.add_url_rule("/apiniveles", 'apiniveles', api.niveles)
app.add_url_rule("/apitalleres", 'apitalleres', api.talleres)
app.add_url_rule("/apinucleos", 'apinucleos', api.nucleos)
API.add_resource(ApiInfo, '/info')
API.add_resource(ApiUser, '/user')
API.add_resource(ApiUserSingle, '/user/<email>')
API.add_resource(ApiUserActivation, '/user/<idU>/<activar>')
API.add_resource(ApiDocente, '/docentes')
API.add_resource(ApiDocenteSingle, '/docentes/<idD>')
API.add_resource(ApiEstudiante, '/estudiante')
API.add_resource(ApiEstudianteSingle, '/estudiante/<idE>')
API.add_resource(ApiInstrumento, '/instrumentos')
API.add_resource(ApiInstrumentoSingle, '/instrumentos/<idI>')
API.add_resource(ApiCiclo_lectivo, '/ciclo_lectivo')
API.add_resource(ApiCiclo_lectivoSingle, '/ciclo_lectivo/<idC>')
API.add_resource(ApiTaller, '/taller')
API.add_resource(ApiTallerSingle, '/taller/<ciclo>/<idT>')
API.add_resource(ApiTallerDocente, '/tallerD/<ciclo>/<taller>/<docente>')
API.add_resource(ApiTallerEstudiante, '/tallerE/<ciclo>/<taller>/<estudiante>')
API.add_resource(ApiHorario, '/horario/<Pciclo>/<Ptaller>/<Pdocente>')
API.add_resource(ApiAsistencia, '/asistencia/<Pciclo>/<Ptaller>/<Pfecha>')
API.add_resource(ApiImg, '/<folder>/<resource>')
app.add_url_rule("/login", 'login', auth.login, methods=['POST'])
app.add_url_rule("/getWithToken", 'getWithToken', auth.getUserWithToken)
