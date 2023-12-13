from flask_restful import reqparse

serializerLogin = reqparse.RequestParser(bundle_errors=True)
serializerLogin.add_argument(
    'correo',
    type=str,
    required=True,
    help='Correo requerido',
    location='json'
)
serializerLogin.add_argument(
    'password',
    type=str,
    required=True,
    help='Contraseña requerida',
    location='json'
)
