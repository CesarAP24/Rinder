from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime

db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()


# Usuario ------------------------------------------------------------------------------------------------

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(36), ForeignKey('perfil.username'))
    correo = db.Column(db.String(50), nullable = False)
    contraseña = db.Column(db.String(100), nullable = False)
    active = db.Column(db.Boolean, default=False)
    likes_restantes = db.Column(db.Integer(), nullable=False)


    # perfil = db.relationship("Perfil", backref="usuario", lazy = True)
    # publicacion = db.relationship("Publicacion", backref="usuario", lazy = True)

    def __repr__(self):
        return f"<Usuario {self.username}, {self.correo}, {self.id_usuario}>"
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "username": self.username,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "active": self.active,
            "likes_restantes": self.likes_restantes
        }

     
# Perfil ------------------------------------------------------------------------------------------------

class Perfil(db.Model):
    __tablename__ = 'perfil'
    username = db.Column(db.String(50), primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    nacimiento = db.Column(db.Date, nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    genero = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    ruta_photo = db.Column(db.String(200))
    created_at = db.Column(db.Date, default=datetime.utcnow())
    modified_at = db.Column(db.Date, default=datetime.utcnow(), onupdate=datetime.utcnow())


    # user = db.relationship('Usuario', backref=db.backref('perfil', lazy=False))

    def __repr__(self):
        return f"<Perfil {self.username}>"

    def serialize(self):
        return {
            "username": self.username,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "nacimiento": self.nacimiento,
            "edad": self.edad,
            "genero": self.genero,
            "descripcion": self.descripcion,
            "ruta_photo": self.ruta_photo,
            "created_at": self.created_at,
            "modified_at": self.modified_at
        }


# Mensaje ------------------------------------------------------------------------------------------------

class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id_mensaje = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_usuarioremitente = db.Column(db.String(50), ForeignKey ('usuario.id_usuario'))
    id_chat = db.Column(db.String(36), ForeignKey ('chat.id_chat'))
    id_mensajePadre = db.Column(db.String(36), ForeignKey ('mensaje.id_mensaje'))


    fecha = db.Column(db.Date, default=lambda: datetime.utcnow())
    contenido = db.Column(db.String(500))
    state = db.Column(db.String(50))
    formato = db.Column(db.String(50))

    def __repr__(self):
        return f"<Mensaje {self.id_mensaje}>"

    def serialize(self):
        return {
            "id_mensaje": self.id_mensaje,
            "id_usuarioremitente": self.id_usuarioremitente,
            "id_chat": self.id_chat,
            "id_mensajePadre": self.id_mensajePadre,
            "fecha": self.fecha,
            "contenido": self.contenido,
            "state": self.state,
            "formato": self.formato
        }    

# CHAT ---------------------------------------------------------------------------------------------------

class Chat(db.Model):
    __table__name= 'chat'
    id_chat = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_usuario = db.Column(db.String(160), ForeignKey('usuario.id_usuario'))
    id_usuario2 = db.Column(db.String(160), ForeignKey('usuario.id_usuario'))
    id_mensaje = db.Column(db.String(160), ForeignKey('mensaje.id_mensaje'))
    fecha = db.Column(db.Date, default=datetime.utcnow(), nullable = False)

    def __repr__(self):
        return f"<Chat {self.id_chat}>"

    def serialize(self):
        return {
            "id_chat": self.id_chat,
            "id_usuario": self.id_usuario,
            "id_usuario2": self.id_usuario2,
            "id_mensaje": self.id_mensaje,
            "fecha": self.fecha
        }



# Suscripcion --------------------------------------------------------------------------------------------

class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'
    nombre = db.Column(db.String(50), primary_key=True)
    precio = db.Column(db.Float, nullable = False)
    created = db.Column(db.Date, default=datetime.utcnow())
    modified = db.Column(db.Date, default=datetime.utcnow(), onupdate=datetime.utcnow()) 
    day_duration = db.Column(db.Integer, default=30)

    def __init__(self, nombre, precio, created, modified, day_duration):
        self.nombre = nombre
        self.precio = precio
        self.created = created
        self.modified = modified
        self.day_duration = day_duration

    def __repr__(self):
        return f"<Suscripcion {self.nombre}>"


# Like --------------------------------------------------------------------------------------------------

class Like(db.Model):
    __tablename__ = 'like'
    id_usuario = db.Column(db.String(50),primary_key=True)
    id_usuario2 = db.Column(db.String(50), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow())

    def __init__(self, id_usuario, id_usuario2, fecha):
        self.id_usuario = id_usuario
        self.id_usuario2 = id_usuario2
        self.fecha = fecha

    def __repr__(self):
        return f"<LikeaPerfil {self.id_usuario}>"
    



# Compra -------------------------------------------------------------------------------------------------

class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    nombre_suscripcion = db.Column(db.String(50), ForeignKey('suscripcion.nombre'))
    fecha = db.Column(db.Date, default=datetime.utcnow())
    precio_compra = db.Column(db.Float, nullable = False)


    def __init__(self, id_usuario, nombre_suscripcion, fecha, precio_compra):
        self.id_usuario = id_usuario
        self.nombre_suscripcion = nombre_suscripcion
        self.fecha = fecha
        self.precio_compra = precio_compra

    def __repr__(self):
        return f"<Compra {self.id_compra}>"