#imports
from flask import(
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
)

from datetime import date
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import datetime


#configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:china@localhost:5432/usuariosRinder'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

    # Usuario(id_usuario: string (primary key), username: string (foreing key), correo: string, contraseña: string, active: bool, likes_restantes: int)

    # Perfil(username:string (primary key), nacimiento:date, edad:int, genero: string, descripcion: string, ruta_photo:string, created_at:date, modified_at:date)

    # Publicacion(id_publicacion: string (primary key), id_usuario:string (foreing key), contenido:string, modified_at:date, created_at:date, cantidad_likes: int)

    # Comentario(id_publicacion: string (primary key), id_usuario:string (primary key), id_publicacion: string (foreign key), id_usuario (foreign key))

    # Post(id_publicacion: string (primary key), id_usuario: string (primary key))


    # Mensajes(id_mensaje:string (primary key), id_usuariodestinatario:string (primary key), id_usuarioremitente:string (primary key), fecha:date, contenido:string, state: string, formato: string, id_mensaje: string (foreign key), id_usuario: string (foreign key), id_usuario: string (foreign key))

    # Suscripcion(nombre:string(primary key), precio: double, created: date, modified: date, duracion: int)

    # RELACIONES


    # Likea_Perfil(id_usuario: string (primary key), id_usuario: string (primary key), created_date: date)

    # Like_Publicacion(id_usuario: string (primary key), id_publicacion: string (primary key), id_usuario: string, created_date: date)

    # Compra(id_usuario: string (primary key), name: string (foreign key), fecha: date, precio_compra: double)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(50), ForeignKey('perfil.username'))
    correo = db.Column(db.String(50), nullable = False)
    contraseña = db.Column(db.String(100), nullable = False)
    active = db.Column(db.Boolean, default=False)
    likes_restantes = db.Column(db.Integer(), nullable=False)
    perfil = db.relationship("Perfil", backref="usuario", lazy = True)
    publicacion = db.relationship("Publicacion", backref="usuario", lazy = True)

    def __init__(self, username, correo, contraseña, active, likes_restantes):
        self.username = username
        self.correo = correo
        self.contraseña = contraseña
        self.active = active
        self.likes_restantes = likes_restantes

    def __repr__(self):
        return f"<Usuario {self.username}>"
        
class Perfil(db.Model):
    __tablename__ = 'perfil'
    username = db.Column(db.String(50), primary_key=True)
    nacimiento = db.Column(db.Date, nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    genero = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(500))
    ruta_photo = db.Column(db.String(200))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    modified_at = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    #la diferncia entre lazy y uselist es que lazy es para cuando es una sola relacion y uselist es para cuando es una lista de relaciones

    user = db.relationship('Usuario', backref=db.backref('perfil', lazy=False))

    def __init__(self, username, nacimiento, edad, genero, descripcion, ruta_photo):
        self.username = username
        self.nacimiento = nacimiento
        self.edad = edad
        self.genero = genero
        self.descripcion = descripcion
        self.ruta_photo = ruta_photo

    def __repr__(self):
        return f"<Perfil {self.username}>"
class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    contenido = db.Column(db.String(500))
    modified_at = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    cantidad_likes = db.Column(db.Integer(), nullable =False, default=0)

    def __init__(self, id_usuario, contenido, modified_at, created_at, cantidad_likes):
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.modified_at = modified_at
        self.created_at = created_at
        self.cantidad_likes = cantidad_likes

    def __repr__(self):
        return f"<Publicacion {self.id_publicacion}>"
    
class Post(db.Model):
    __tablename__ = 'post'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    def __init__(self, id_publicacion):
        self.id_publicacion = id_publicacion
    def __repr__(self):
        return f"<Post {self.id_publicacion}>"
    
    
class Comentario(db.Model):
    __tablename__ = 'comentario'
    id_publicacion = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4())) 
    id_publicacion2 = db.Column(db.String(36), primary_key = True, default=str(uuid.uuid4()))
   
    def __init__(self, id_publicacion, id_publicacion2):
        self.id_publicacion = id_publicacion
        self.id_publicacion2 = id_publicacion2
       
    def __repr__(self):
        return f"<Comentario {self.id_publicacion}>"
    
class Mensaje(db.Model):
    __tablename__ = 'mensaje'
    id_mensaje = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_mensaje2 = db.Column(db.String(36), ForeignKey ('mensaje.id_mensaje'))

    id_usuariodestinatario = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    id_usuariodestinatario2 = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    
    id_usuarioremitente = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    id_usuarioremitente2 = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    
    fecha = db.Column(db.Date, default=datetime.utcnow)
    contenido = db.Column(db.String(500))
    state = db.Column(db.String(50))
    formato = db.Column(db.String(50))

    def __init__(self, id_usuariodestinatario, id_usuarioremitente, fecha, contenido, state, formato):
        self.id_usuariodestinatario = id_usuariodestinatario
        self.id_usuarioremitente = id_usuarioremitente
        self.fecha = fecha
        self.contenido = contenido
        self.state = state
        self.formato = formato

    def __repr__(self):
        return f"<Mensaje {self.id_mensaje}>"
    
class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'
    nombre = db.Column(db.String(50), primary_key=True)
    precio = db.Column(db.Float)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow)
    duracion = db.Column(db.Integer())

    def __init__(self, nombre, precio, created, modified, duracion):
        self.nombre = nombre
        self.precio = precio
        self.created = created
        self.modified = modified
        self.duracion = duracion

    def __repr__(self):
        return f"<Suscripcion {self.nombre}>"
    
class Likea_Perfil(db.Model):
    __tablename__ = 'likea_perfil'
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'), primary_key=True)
    id_perfil = db.Column(db.String(50), ForeignKey('perfil.username'), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, id_usuario, id_perfil, fecha):
        self.id_usuario = id_usuario
        self.id_perfil = id_perfil
        self.fecha = fecha

    def __repr__(self):
        return f"<LikeaPerfil {self.id_usuario}>"
    
class Likea_Publicacion(db.Model):
    __tablename__ = 'likea_publicacion'
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'), primary_key=True)
    id_publicacion = db.Column(db.String(36), ForeignKey('publicacion.id_publicacion'), primary_key=True)
    fecha = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, id_usuario, id_publicacion, fecha):
        self.id_usuario = id_usuario
        self.id_publicacion = id_publicacion
        self.fecha = fecha

    def __repr__(self):
        return f"<LikeaPublicacion {self.id_usuario}>"
class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    id_usuario = db.Column(db.String(50), ForeignKey('usuario.id_usuario'))
    nombre_suscripcion = db.Column(db.String(50), ForeignKey('suscripcion.nombre'))
    fecha = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, id_usuario, nombre_suscripcion, fecha):
        self.id_usuario = id_usuario
        self.nombre_suscripcion = nombre_suscripcion
        self.fecha = fecha

    def __repr__(self):
        return f"<Compra {self.id_compra}>"
    










