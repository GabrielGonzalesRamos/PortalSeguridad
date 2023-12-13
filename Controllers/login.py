from flask_restful import Resource
from flask_jwt_extended import create_access_token
from Config.conexion_bd import base_de_datos
from Models.usuario import UsuarioModel
from Serializers.serializerLogin import serializerLogin
from bcrypt import checkpw

class LoginController(Resource):

    def post(self):
        data = serializerLogin.parse_args()
        usuario = base_de_datos.session.query(UsuarioModel).filter_by(usuarioCorreo=data.get('correo')).first()
        if not usuario:
            return {
                'success': False,
                'content': None,
                'message': 'El usuario no existe. Por favor, verificar el correo o registrarse uno nuevo si es necesario.'
                }, 400
        
        if checkpw(bytes(data.get('password'), 'utf-8'), bytes(usuario.usuarioPassword, 'utf-8')): 
            token = create_access_token(
                identity=usuario.usuarioId, additional_claims={
                'nombre': usuario.usuarioNombre,
                'apellido': usuario.usuarioApellido,
                'correo': usuario.usuarioCorreo                  
            })
            return {
                'success': True,
                'content': token,
                'message': 'Inicio de sesión exitoso'
                }, 201
        else: 
            return {
                'success': False,
                'content': None,
                'message': "La contraseña ingresada no coincide con la del usuario. Por favor, verifica la contraseña e inténtalo nuevamente. Si olvidaste tu contraseña, puedes restablecerla siguiendo las instrucciones correspondientes."
                }, 400
                




