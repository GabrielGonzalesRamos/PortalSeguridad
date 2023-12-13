from Config.conexion_bd import base_de_datos
from sqlalchemy import Column, types, UniqueConstraint, CheckConstraint
from bcrypt import hashpw, gensalt


class UsuarioModel(base_de_datos.Model):
    __tablename__ = 'tb_usuario'
    usuarioId = Column(name='id', autoincrement=True, primary_key=True, unique=True, type_=types.Integer, nullable=False)
    usuarioNombre = Column(name='nombre', type_=types.String(length=60), nullable=False)
    usuarioApellido = Column(name='apellido', type_=types.String(length=60), nullable=False)
    usuarioCorreo = Column(name='correo', type_=types.String(length=120), nullable=False)
    usuarioPassword = Column(name='password', type_=types.TEXT, nullable=False)

    __table_args__ = (
        UniqueConstraint('correo', name='avoid_duplicate_correo'),
        CheckConstraint('correo ~ \'^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$\'', name='validate_profesional_correo')
    )

    def __init__(self, nombre, apellido, correo, password):
        self.usuarioNombre = nombre
        self.usuarioApellido = apellido
        self.usuarioCorreo = correo
        passwordHash = hashpw(bytes(password, "utf-8"), gensalt())
        self.usuarioPassword = passwordHash.decode("utf-8")
    
    def save(self):
        base_de_datos.session.add(self)
        base_de_datos.session.commit()

    def json(self):
        return {
            'nombre': self.usuarioNombre,
            'apellido': self.usuarioApellido,
            'correo': self.usuarioCorreo
        }
