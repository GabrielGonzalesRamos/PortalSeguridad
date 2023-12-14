from flask_restful import Resource, reqparse
from datetime import datetime

serializerAlumnos = reqparse.RequestParser(bundle_errors=True)
serializerAlumnos.add_argument(
    'dni',
    type=str,
    required=True,
    help='El campo "dni" es requerido para procesar la solicitud.',
    location='json'
)
serializerAlumnos.add_argument(
    'nombre',
    type=str,
    required=True,
    help='El campo "nombre" es requerido para procesar la solicitud.',
    location='json'
)
serializerAlumnos.add_argument(
    'apellido',
    type=str,
    required=True,
    help='El campo "apellido" es requerido para procesar la solicitud.',
    location='json'
)
serializerAlumnos.add_argument(
    'direccion',
    type=str,
    required=True,
    help='El campo "direccion" es requerido para procesar la solicitud.',
    location='json'
)
serializerAlumnos.add_argument(
    'pais',
    type=str,
    required=True,
    help='El campo "pais" es requerido para procesar la solicitud. Asegurese de incluir el campo o veriricar que sea un país válido',
    location='json'
)
serializerAlumnos.add_argument(
    'fecha_nacimiento',
    type=lambda x: datetime.strptime(x,"%Y-%m-%d"),
    required=True,
    help='El campo "fecha_nacimiento" es requerido para procesar la solicitud',
    location='json'
)