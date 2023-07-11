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

from flask_jwt_extended import JWTManager, jwt_required, create_access_token
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
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis';
    app.config['JWT_SECRET_KEY'] = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    bcrypt = Bcrypt(app);
    jwt = JWTManager(app);
    
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response
















    # Routes API

    # GET ------------------------------------------------------------------
    @app.route('/mensajes', methods=['GET'])
    def get_mensajes():
        abort(501)

    @app.route('/chats', methods=['GET'])
    def get_chats():
        abort(501)

    @app.route('/perfiles', methods=['GET'])
    def get_perfil():
        abort(501)

    @app.route('/suscripciones', methods=['GET'])
    def get_suscriptions():
        abort(501)

    @app.route('/compras', methods=['GET'])
    def get_compras():
        abort(501)

    # PATCH ----------------------------------------------------------------

    @app.route('/perfiles', methods=['PATCH'])
    def patch_perfil():
        abort(501)

    @app.route('/usuarios', methods=['PATCH'])
    def patch_users():
        abort(501)

    @app.route('/compras', methods=['PATCH'])
    def patch_compras():
        abort(501)































    # POST -----------------------------------------------------------------

    @app.route('/usuarios', methods=['POST'])
    def post_users():
        abort(501)

    @app.route('/mensajes', methods=['POST'])
    def post_mensajes():
        abort(501)


    @app.route('/suscripciones', methods=['POST'])
    def post_suscriptions():
        abort(501)

    @app.route('/chats', methods=['POST'])
    def post_compras():
        abort(501)

    @app.route('/compras', methods=['POST'])
    def post_compras():
        abort(501)

    @app.route('/likes', methods=['POST'])
    def post_likes():
        abort(501)

    

    # DELETE ---------------------------------------------------------------

    @app.route('/usuarios', methods=['DELETE'])
    def delete_users():
        abort(501)

    @app.route('/suscripciones', methods=['DELETE'])
    def delete_suscriptions():
        abort(501)



    # LOGIN ----------------------------------------------------------------

    @app.route('/api/login', methods=['POST'])
    def login():
        abort(501)
    
















    # HANDLE ERROR ---------------------------------------------------------

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({ "success": False, "message": 'Resource not found' }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({ "success": False, "message": 'Unauthorized' }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({ "success": False, "message": 'Bad request' }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({ "success": False, "message": 'Method not allowed' }), 405

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({ "success": False, "message": 'Forbidden' }), 403


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({ "success": False, "message": 'Server error' }), 500

    @app.errorhandler(501)
    def not_implemented(error):
        return jsonify({ "success": False, "message": 'Not implemented' }), 501

    return app

