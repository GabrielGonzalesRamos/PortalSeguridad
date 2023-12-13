from flask_restful import reqparse

serializerLogin = reqparse.RequestParser(bundle_errors=True)
serializerLogin.add_argument(
    'correo',
    type=str,
    required=True,
    help='Por favor, asegúrate de completar el campo del correo para continuar',
    location='json'
)
serializerLogin.add_argument(
    'password',
    type=str,
    required=True,
    help='Por favor, asegúrate de ingresar tu contraseña para continuar.',
    location='json'
)
