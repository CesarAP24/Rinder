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
    id_usuario = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(36), ForeignKey('perfil.username'))
    correo = db.Column(db.String(50), nullable = False)
    contraseña = db.Column(db.String(100), nullable = False)
    active = db.Column(db.Boolean, default=False)
    likes_restantes = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}, {self.correo}, {self.id_usuario}>"


     
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

    def __repr__(self):
        return f"<Perfil {self.username}>"


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




# Suscripcion --------------------------------------------------------------------------------------------

class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'
    nombre = db.Column(db.String(50), primary_key=True)
    precio = db.Column(db.Float, nullable = False)
    created = db.Column(db.Date, default=datetime.utcnow())
    modified = db.Column(db.Date, default=datetime.utcnow(), onupdate=datetime.utcnow()) 
    day_duration = db.Column(db.Integer, default=30)

    def __repr__(self):
        return f"<Suscripcion {self.nombre}>"


# Like --------------------------------------------------------------------------------------------------

class Like(db.Model):
    __tablename__ = 'like'
    id_usuario = db.Column(db.String(50),primary_key=True)
    id_usuario2 = db.Column(db.String(50), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow())


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

    def __repr__(self):
        return f"<Compra {self.id_compra}>"