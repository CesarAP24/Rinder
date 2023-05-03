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

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)

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

