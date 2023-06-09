from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import sys



db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()


# Usuario ------------------------------------------------------------------------------------------------

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    correo = db.Column(db.String(50), nullable = False, unique=True)
    contraseña = db.Column(db.String(300), nullable = False)

    #metodo para verificar la contraseña hasheada
    def check_password(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)


    def delete(self):
        returned_code = 200
        try:
            its_pertenencias = Pertenece.query.filter_by(id_usuario=self.id_usuario).all()

            for pertenencia in its_pertenencias:
                chat = Chat.query.filter_by(id_chat=pertenencia.id_chat).first()
                if chat:
                    chat.id_mensaje = "default"
                    db.session.commit()
                db.session.delete(pertenencia)

            its_mensajes = Mensaje.query.filter_by(id_usuario=self.id_usuario).all()
            for mensaje in its_mensajes:
                db.session.delete(mensaje)


            its_perfil = Perfil.query.filter_by(id_usuario=self.id_usuario).first()
            if its_perfil:
                db.session.delete(its_perfil)

            its_likes = Like.query.filter_by(id_usuario=self.id_usuario).all()
            for like in its_likes:
                db.session.delete(like)

            #deletear con cascada
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())
            returned_code = 500

        return returned_code


    def insert(self):
        user_id = "None"
        try:
            db.session.add(self)
            db.session.commit()
            user_id = self.id_usuario
        except:
            db.session.rollback()
            print(sys.exc_info())

        return user_id


    def __init__(self, correo, contraseña, id_usuario=None):
        self.correo = correo
        self.contraseña = generate_password_hash(contraseña)
        if id_usuario:
            self.id_usuario = id_usuario
        else:
            self.id_usuario = str(uuid.uuid4())

    def __repr__(self):
        return f"<Usuario {self.correo}, {self.id_usuario}>"

     
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

    def serialize(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'nacimiento': self.nacimiento,
            'genero': self.genero,
            'descripcion': self.descripcion,
            'ruta_photo': self.ruta_photo,
            'correo': Usuario.query.get(self.id_usuario).correo if Usuario.query.get(self.id_usuario) else None,
        }


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

    def serialize(self):
        return {
            'id_mensaje': self.id_mensaje,
            'id_usuario': self.id_usuario,
            'id_chat': self.id_chat,
            'id_mensajePadre': self.id_mensajePadre,
            'fecha': self.fecha,
            'contenido': self.contenido,
            'state': self.state
        }
 

# CHAT ---------------------------------------------------------------------------------------------------

class Chat(db.Model):
    __table__name= 'chat'
    id_chat = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_mensaje = db.Column(db.String(160), ForeignKey('mensaje.id_mensaje'))
    cantidad_mensajes = db.Column(db.Integer, default=0)
    fecha = db.Column(db.DateTime, default=datetime.utcnow(), nullable = False)

    def __repr__(self):
        return f"<Chat {self.id_chat}>"

    def serialize(self):
        return {
            'id_chat': self.id_chat,
            'id_mensaje': self.id_mensaje,
            'cantidad_mensajes': self.cantidad_mensajes,
            'fecha': self.fecha
        }

class Pertenece(db.Model):
    __tablename__ = 'pertenece'
    id_usuario = db.Column(db.String(36), ForeignKey('usuario.id_usuario'), primary_key=True)
    id_chat = db.Column(db.String(36), ForeignKey('chat.id_chat'), primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow(), nullable = False)

    def __repr__(self):
        return f"<Pertenece {self.id_chat}>"

    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'id_chat': self.id_chat,
            'fecha': self.fecha
        }

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

    def serialize(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'day_duration': self.day_duration
        }

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

    def serialize(self):
        return {
            'id_compra': self.id_compra,
            'suscripcion': self.suscripcion,
            'fecha': self.fecha,
            'precio_compra': self.precio_compra
        }

