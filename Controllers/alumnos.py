from flask import request
from flask_restful import Resource
from Serializers.serializerAlumnos import serializerAlumnos
from flask_jwt_extended import jwt_required, get_jwt

class AlumnosController(Resource):
    @jwt_required()
    def post(self):
        print(get_jwt())
        print(request.method)
