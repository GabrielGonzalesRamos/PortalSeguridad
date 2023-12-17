from flask_jwt_extended import JWTManager

jwt = JWTManager()

@jwt.expired_token_loader
def expired_token_callback(jwt_required, jwt_payload):
    return {
        'success': False,
        'content': None,
        'message': 'Su token de autenticación ha expirado. Por favor, vuelva a iniciar sesión para obtener un nuevo token '
    }, 401

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return {
        'success': False,
        'content': None,
        'message': 'Acceso denegado. Esta ruta requiere un token de autenticación válido para acceder'
    }, 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return {
        'success': False,
        'content': None,
        'message': 'El token de autenticación enviado es inválido o ha sido alterado'
    }, 401