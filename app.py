#imports
import psycopg2 
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


#configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:china@localhost:5432/usuariosRinder'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class suscripcion(db.Model):
    __tablename__ = 'suscripciones'
    name = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    usuarios = db.relationship('User', backref='suscripcion', lazy=True)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True, server_default='true')
    likes_restantes = db.Column(db.Integer, nullable=False, default=3)
    name_suscripcion = db.Column(db.string, ForeignKey('suscripciones.name'), nullable=False)
    id_perfil = db.Column(db.Integer, ForeignKey('perfiles.id'), nullable=False)
    


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(300), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    id_message_parent = db.Column(db.Integer, ForeignKey('messages.id'), nullable=True)


class Perfil(db.Model):
    __tablename__ = 'perfiles'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(300), nullable=False)
    id_usuario = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    usuario= db.relationship('User', backref='perfiles', lazy=True)

# ... código para configurar Flask y SQLAlchemy ...

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
    fecha_nacimiento = request.form['fecha_nacimiento']

    # Calcular la edad a partir de la fecha de nacimiento
    hoy = date.today()
    fecha_nacimiento = date.fromisoformat(fecha_nacimiento)
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    # Verificar que el usuario tenga al menos 18 años
    if edad < 18:
        return render_template('login.html', mensaje_edad='Debes tener al menos 18 años para registrarte.')

    # Crear y guardar el nuevo usuario
    nuevo_usuario = User(nombre=nombre, email=email, password=password, fecha_nacimiento=fecha_nacimiento)
    db.session.add(nuevo_usuario)
    db.session.commit()

    # Redirigir al usuario a la página principal
    return redirect('index.html')

