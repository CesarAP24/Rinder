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
import uuid;


#configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:china@localhost:5432/usuariosRinder'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class suscripcion(db.Model):
    __tablename__ = 'suscripciones'
    #keys
    name = db.Column(db.String(50), primary_key=True)
    
    precio = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    usuarios = db.relationship('User', backref='suscripcion', lazy=True)
    compras = db.relationship('compra', backref='suscripcion', lazy=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)

    nombre = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True, server_default='true')
    name_suscripcion = db.Column(db.String(50), ForeignKey('suscripciones.name'), nullable=False)
    id_perfil = db.Column(db.Integer, ForeignKey('perfiles.id'), nullable=False)
    

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.string(50), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    id_message_parent = db.Column(db.Integer, ForeignKey('messages.id'), nullable=True)
    
    texto = db.Column(db.String(300), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    


class Perfil(db.Model):
    __tablename__ = 'perfiles'
    #keys and foreing keys
    id_usuario = db.Column(db.String(50), ForeignKey('users.id'), nullable=False)
    usuario= db.relationship('User', backref='perfiles', lazy=True)
    
    #atributes
    username = db.Column(db.String(50), nullable=False)
    edad= db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    likes_restantes = db.Column(db.Integer, nullable=False, default=3)
    language = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    ruta_foto= db.Column(db.String(300), nullable=False)
    
    #necessary extra
    modified_at = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.Date, nullable=False)


class publicacion(db.Model):
    __tablename__ = 'publicaciones'

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(300), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    kindofpost= db.Column(db.String(300), nullable=False)
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    id_message_parent = db.Column(db.Integer, ForeignKey('messages.id'), nullable=True)
    usuario= db.relationship('User', backref='publicaciones', lazy=True)



class compra(db.Model):
    __table__name = 'compras'
    precio= db.Column(db.Integer, nullable=False)
    suscripcion_name= db.Column(db.String(50), ForeignKey('suscripciones.name'), nullable=False)
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    usuario= db.relationship('User', backref='compras', lazy=True)
    suscripcion= db.relationship('suscripcion', backref='compras', lazy=True)



class like(db.Model): 
    __table__name = 'likes'
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    id_publicacion = db.Column(db.Integer, ForeignKey('publicaciones.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    usuario= db.relationship('User', backref='likes', lazy=True)
    publicacion= db.relationship('publicacion', backref='likes', lazy=True)



# ... ROUTES ...

@app.route('/Usuarios', methods=['POST', 'GET'])
def procesar_registro():
    if request.method == 'POST':
        # FALTA IMPLEMENTAR va a depender de lo que desee isabella :v
        return (jsonify({'error': 'Método no implementado'}), 501);

    elif request.method == 'GET':
        # Devolver todos los ids de los usuarios existentes
        usuarios = User.query.all()

        usuarios_json = [usuario.id for usuario in usuarios]

        return (jsonify(usuarios_json), 200);

    elif request.method == 'PATCH':
        # FALTA IMPLEMENTAR
        return (jsonify({'message': 'Método no implementado'}), 501);

    elif request.method == 'DELETE':

        # Verificar que se tenga permisos
        if not request.headers.get('Authorization'):
            return (jsonify({'message': 'No tienes permisos para realizar esta acción'}), 403);
        else:
            # verificar FALTA IMPLEMENTAR
            return (jsonify(usuarios_json), 200);
            pass

        # ELimina TODOS los usuarios
        usuarios = User.query.all();

        with app.app_context():
            for usuario in usuarios:
                db.session.delete(usuario);
            db.session.commit();

        return (jsonify({'message': 'Todos los usuarios han sido eliminados'}), 200);

    else:
        return render_template('error.html', error={"name":"Error 404", "message":"Página no encontrada"}), 404;


@app.route('/Usuarios/<id>', methods=['GET', 'DELETE', 'PATCH'])
def procesar_usuario(id):
    if request.method == 'GET':
        # Verificar que el usuario exista
        usuario = User.query.filter_by(id=id).first();

        if not usuario:
            return (jsonify({'message': 'El usuario no existe'}), 404);

        # Devolver los datos del usuario
        usuario_json = {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'fecha_nacimiento': usuario.fecha_nacimiento,
            'is_active': usuario.is_active,
            'likes_restantes': usuario.likes_restantes,
            'name_suscripcion': usuario.name_suscripcion,
        }

        return (jsonify(usuario_json), 200);

    elif request.method == 'DELETE':
        # Verificar que el usuario exista
        usuario = User.query.filter_by(id=id).first();

        if not usuario:
            return (jsonify({'message': 'El usuario no existe'}), 404);

        # Verificar que se tenga permisos
        if not request.headers.get('Authorization'):
            return (jsonify({'message': 'No tienes permisos para realizar esta acción'}), 403);
        else:
            # verificar FALTA IMPLEMENTAR
            pass

        # Eliminar el usuario
        with app.app_context():
            db.session.delete(usuario);
            db.session.commit();

        return (jsonify({'message': 'El usuario ha sido eliminado'}), 200);

    elif request.method == 'PATCH':
        # FALTA IMPLEMENTAR
        return (jsonify({'message': 'Método no implementado'}), 501);


@app.route('/Usuarios/<id>/Perfiles', methods=['GET', 'PATCH'])
def procesar_perfiles(id):
    #permisos
    if request.method == 'GET':
        #devolver el perfil
        pass
    elif request.method == 'PATCH':
        #MODIFICAR VALORES DEL PERFIL
        pass
    else:
        #metodo no permitido
        render_template('error.html', error={"name":"Método no permitido", "description":"El método que se está intentando usar no está permitido en esta ruta."})



