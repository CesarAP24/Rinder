from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey



db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()


# Usuario ------------------------------------------------------------------------------------------------

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.String(36), primary_key=True)
    correo = db.Column(db.String(50), nullable = False, unique=True)
    contraseña = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f"<Usuario {self.username}, {self.correo}, {self.id_usuario}>"


     
# Perfil ------------------------------------------------------------------------------------------------

class Perfil(db.Model):
    __tablename__ = 'perfil'
    id_usuario = db.Column(db.String(36),ForeignKey('usuario.id_usuario'), primary_key=True)

    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    nacimiento = db.Column(db.Date, nullable = False)
    genero = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    ruta_photo = db.Column(db.String(200))
    ruta_network = db.Column(db.String(200))
    likes_restantes = db.Column(db.Integer, default=20)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    modified_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return f"<Perfil {self.username}>"


# Mensaje ------------------------------------------------------------------------------------------------

class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id_mensaje = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_usuario = db.Column(db.String(36), ForeignKey ('usuario.id_usuario'))
    id_chat = db.Column(db.String(36), ForeignKey ('chat.id_chat'))
    id_mensajePadre = db.Column(db.String(36), ForeignKey ('mensaje.id_mensaje'))


    fecha = db.Column(db.DateTime, default=lambda: datetime.utcnow(), nullable = False)
    contenido = db.Column(db.String(5000))
    state = db.Column(db.String(50), default='0') # 0: enviado, 1: recibido, 2: leido

    def __repr__(self):
        return f"<Mensaje {self.id_mensaje}>"
 

# CHAT ---------------------------------------------------------------------------------------------------

class Chat(db.Model):
    __table__name= 'chat'
    id_chat = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_mensaje = db.Column(db.String(160), ForeignKey('mensaje.id_mensaje'))
    cantidad_mensajes = db.Column(db.Integer, default=0)
    fecha = db.Column(db.DateTime, default=datetime.utcnow(), nullable = False)

    def __repr__(self):
        return f"<Chat {self.id_chat}>"



class Pertenece(db.Model):
    __tablename__ = 'pertenece'
    id_usuario = db.Column(db.String(36), ForeignKey('usuario.id_usuario'), primary_key=True)
    id_chat = db.Column(db.String(36), ForeignKey('chat.id_chat'), primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow(), nullable = False)

    def __repr__(self):
        return f"<Pertenece {self.id_chat}>"


# Suscripcion --------------------------------------------------------------------------------------------

class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'
    nombre = db.Column(db.String(50), primary_key=True)
    precio = db.Column(db.Float, nullable = False)
    day_duration = db.Column(db.Integer, default=30)

    created = db.Column(db.DateTime, default=datetime.utcnow())
    modified = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()) 

    def __repr__(self):
        return f"<Suscripcion {self.nombre}>"

# Like --------------------------------------------------------------------------------------------------

class Like(db.Model):
    __tablename__ = 'like'
    id_usuario = db.Column(db.String(50),primary_key=True)
    id_usuario_likeado = db.Column(db.String(50), primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow())


    def __repr__(self):
        return f"<LikeaPerfil {self.id_usuario}>"


# Compra -------------------------------------------------------------------------------------------------

class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))

    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    suscripcion = db.Column(db.String(50), ForeignKey('suscripcion.nombre'))
    fecha = db.Column(db.DateTime, default=datetime.utcnow())
    precio_compra = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return f"<Compra {self.id_compra}>"

