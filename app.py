# IMPORTS ------------------------------------------------------------------------------------------------
# ========================================================================================================

# flask --------------------------------------------------------------------------------------------------

from flask import(
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

# libraries ----------------------------------------------------------------------------------------------

import uuid
from datetime import datetime


# CONFIGURATIONS -----------------------------------------------------------------------------------------
# ========================================================================================================

app = Flask(__name__)
app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis';
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3028222024@localhost:5432/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# MODEL --------------------------------------------------------------------------------------------------
# ========================================================================================================


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



# Publicacion -------------------------------------------------------------------------------------------

class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    contenido = db.Column(db.String(500))
    modified_at = db.Column(db.Date, default=datetime.utcnow(), onupdate=datetime.utcnow())
    created_at = db.Column(db.Date, default=datetime.utcnow())
    cantidad_likes = db.Column(db.Integer(), nullable =False, default=0)

    def __init__(self, id_usuario, contenido, modified_at, created_at, cantidad_likes):
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.modified_at = modified_at
        self.created_at = created_at
        self.cantidad_likes = cantidad_likes

    def __repr__(self):
        return f"<Publicacion {self.id_publicacion}>"
    


# Pub/Post

class Post(db.Model):
    __tablename__ = 'post'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    def __init__(self, id_publicacion):
        self.id_publicacion = id_publicacion
    def __repr__(self):
        return f"<Post {self.id_publicacion}>"
    
    

# Pub/Comentario 

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4())) 
    id_publicacion2 = db.Column(db.String(36), ForeignKey ('publicacion.id_publicacion'))

   
    def __init__(self, id_publicacion, id_publicacion2):
        self.id_publicacion = id_publicacion
        self.id_publicacion2 = id_publicacion2
       
    def __repr__(self):
        return f"<Comentario {self.id_publicacion}>"
    


# Mensaje ------------------------------------------------------------------------------------------------

class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id_mensaje = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_usuariodestinatario = db.Column(db.String(50), ForeignKey ('usuario.id_usuario'))
    id_usuarioremitente = db.Column(db.String(50), ForeignKey ('usuario.id_usuario'))
    
    id_mensaje2 = db.Column(db.String(36), ForeignKey ('mensaje.id_mensaje'))

    

    fecha = db.Column(db.Date, default=datetime.utcnow())
    contenido = db.Column(db.String(500))
    state = db.Column(db.String(50))
    formato = db.Column(db.String(50))

    def __init__(self, id_mensaje, id_mensaje2, id_usuariodestinatario, id_usuariodestinatario2, id_usuarioremitente, id_usuarioremitente2, fecha, contenido, state, formato ):
        self.id_mensaje = id_mensaje
        self.id_mensaje2 = id_mensaje2
        self.id_usuariodestinatario = id_usuariodestinatario
        self.id_usuariodestinatario2 = id_usuariodestinatario2
        self.id_usuarioremitente = id_usuarioremitente
        self.id_usuarioremitente2 = id_usuarioremitente2
        self.fecha = fecha
        self.contenido = contenido
        self.state = state
        self.formato = formato


    def __repr__(self):
        return f"<Mensaje {self.id_mensaje}>"
    


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
    


# Likea --------------------------------------------------------------------------------------------------

class Likea_Perfil(db.Model):
    __tablename__ = 'likea_perfil'
    id_usuario = db.Column(db.String(50),primary_key=True)
    id_usuario2 = db.Column(db.String(50), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow())

    def __init__(self, id_usuario, id_usuario2, fecha):
        self.id_usuario = id_usuario
        self.id_usuario2 = id_usuario2
        self.fecha = fecha

    def __repr__(self):
        return f"<LikeaPerfil {self.id_usuario}>"
    

class Likea_Publicacion(db.Model):
    __tablename__ = 'likea_publicacion'
    id_usuario = db.Column(db.String(50), primary_key=True)
    id_usuario2 =  db.Column(db.String(50), primary_key=True)
    id_publicacion = db.Column(db.String(36), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow())

    def __init__(self, id_usuario, id_usuario2, id_publicacion, fecha):
        self.id_usuario = id_usuario
        self.id_usuario2 = id_usuario2
        self.id_publicacion = id_publicacion
        self.fecha = fecha
    

    def __repr__(self):
        return f"<LikeaPublicacion {self.id_usuario}>"



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







# routes -------------------------------------------------------------------------------------------------

from routes import *

