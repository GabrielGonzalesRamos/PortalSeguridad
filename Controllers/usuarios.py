from re import search
from flask_restful import Resource
from Models.usuario import UsuarioModel
from Serializers.serializerUsuarios import serializerUsuarios

class UsuariosController(Resource):
    
    def post(self):
        data = serializerUsuarios.parse_args()
        nuevoUsuario = UsuarioModel(\
            nombre=data.get('nombre'), \
            apellido=data.get('apellido'), \
            correo=data.get('correo'), \
            password=data.get('password') \
            )
        if not search('^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$',data.get('correo')):
            return {
                'success': False,
                'content': None,
                'message': 'Ingrese un correo válido'
                }, 400
        if not search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', data.get('password')):
            return {
                'success': False,
                'content': None,
                'message': 'La contraseña debe tener al menos 8 caracteres, incluyendo al menos una letra mayúscula, una minúscula, un número y un carácter especial.'
            }, 400
        try:
            nuevoUsuario.save()
            return {
                'success': True,
                'content': nuevoUsuario.json(),
                'message': 'Usuario registrado exitosamente'     
            }, 201
        except Exception as E:
            print(E)
            return {
                'success': False,
                'content': None,
                'message': 'Correo registrado previamente'
            }, 400





            