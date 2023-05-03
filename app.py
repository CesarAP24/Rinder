#imports
import psycopg2 
from flask import(
    Flask,
    render_template,
    jsonify,
    request,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Goleador0107@localhost:5432/rinder'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
