# Libraries

from .models import *
from flask_cors import CORS
from .utilities import *

from flask import(
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    abort,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

import uuid
import json
from datetime import datetime
from flask_bcrypt import Bcrypt



# App

def create_app(test_config=None):
    app = Flask(__name__)
    app = Flask(__name__)
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis';
    bcrypt = Bcrypt(app);
    
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/employees'
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response


    # Routes API


    # Handle Error

    return app

