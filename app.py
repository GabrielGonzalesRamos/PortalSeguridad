from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from Config.conexion_bd import base_de_datos
from Controllers.usuarios import UsuariosController
from Controllers.login import LoginController
from Controllers.alumnos import AlumnosController
from datetime import timedelta
from os import environ

load_dotenv()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI_PROD')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=1)

jwt = JWTManager(app)

base_de_datos.init_app(app)
base_de_datos.create_all(app=app)

api = Api(app)
api.add_resource(UsuariosController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(AlumnosController, '/alumnos')

CORS(app=app, methods=['POST', 'GET', 'PUT', 'DELETE'], origins=['*'], allow_headers=['Content-Type'])

if __name__ == '__main__':
    app.run(debug=True, port=5005)