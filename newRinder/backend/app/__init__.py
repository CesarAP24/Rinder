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

    # GET ------------------------------------------------------------------
    @app.route('/users', methods=['GET'])
    def get_users():
        abort(501)

    @app.route('/profiles', methods=['GET'])
    def get_profiles():
        abort(501)

    @app.route('/messages', methods=['GET'])
    def get_mensaje():
        abort(501)

    @app.route('/chat', methods=['GET'])
    def get_chat():
        abort(501)

    @app.route('/suscriptions', methods=['GET'])
    def get_suscriptions():
        abort(501)

    @app.route('/likes', methods=['GET'])
    def get_likes():
        abort(501)

    @app.route('/purchases', methods=['GET'])
    def get_purchases():
        abort(501)

    # POST -----------------------------------------------------------------

    @app.route('/users', methods=['POST'])
    def post_users():
        abort(501)

    @app.route('/profiles', methods=['POST'])
    def post_profile():
        abort(501)

    @app.route('/messages', methods=['POST'])
    def post_mensaje():
        abort(501)

    @app.route('/chats', methods=['POST'])
    def post_chat():
        abort(501)

    @app.route('/suscriptions', methods=['POST'])
    def post_suscriptions():
        abort(501)

    @app.route('/likes', methods=['POST'])
    def post_likes():
        abort(501)

    @app.route('/purchases', methods=['POST'])
    def post_purchases():
        abort(501)

    

    # PATCH ----------------------------------------------------------------

    @app.route('/users/<id>', methods=['PATCH'])
    def patch_users(id):
        abort(501)

    @app.route('/profiles/<id>', methods=['PATCH'])
    def patch_profile(id):
        abort(501)

    @app.route('chats/<id>', methods=['PATCH'])
    def patch_chat(id):
        abort(501)

    @app.route('/suscriptions/<id>', methods=['PATCH'])
    def patch_suscriptions(id):
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

