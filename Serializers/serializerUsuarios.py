from flask_restful import reqparse

serializerUsuarios = reqparse.RequestParser(bundle_errors=True)
serializerUsuarios.add_argument(
    'nombre',
    type=str,
    required=True,
    help='Nombre del usuario requerido',
    location='json'
)
serializerUsuarios.add_argument(
    'apellido',
    type=str,
    required=True,
    help='Apellido del usuario requerido',
    location='json'
)
serializerUsuarios.add_argument(
    'correo',
    type=str,
    required=True,
    help='Correo del usuario requerido',
    location='json'
)
serializerUsuarios.add_argument(
    'password',
    type=str,
    required=True,
    help='Password del usuario requerido',
    location='json'
)