# Libraries

from .models import db, Usuario, Perfil, Chat, Mensaje, Suscripcion, Compra, Like
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
    @app.route('/chats/<id>/mensajes', methods=['GET'])
    @jwt_required
    def get_mensajes(id):
        chat = Chat.query.filter_by(id_chat=id).first()
        user_id = get_jwt_identity()

        #checkear si el usuario participa en el chat
        chats = Pertenece.query.filter_by(id_usuario=user_id).all()
        id_chats = [chat.id_chat for chat in chats]

        if chat.id_chat in id_chats:
            mensajes = Mensaje.query.filter_by(id_chat=id).all()
            return jsonify({
                'success': True,
                'mensajes': [mensaje.serialize() for mensaje in mensajes]
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'El usuario no participa en el chat'
            }), 401



    @app.route('/chats', methods=['GET'])
    @jwt_required
    def get_chats():
        user_id = get_jwt_identity()
        chats = Pertenece.query.filter_by(id_usuario=user_id).all()

        if chats:
            id_chats = [chat.id_chat for chat in chats]
            chats = Chat.query.filter(Chat.id_chat.in_(id_chats)).all()
            return jsonify({
                'success': True,
                'chats': [chat.serialize() for chat in chats]
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'El usuario no tiene chats'
            }), 404


    @app.route('/perfiles', methods=['GET'])
    def get_perfil():
        perfiles = Perfil.query.all()
        return jsonify({
            'success': True,
            'perfiles': [perfil.serialize() for perfil in perfiles]
        }), 200

    

    @app.route('/suscripciones', methods=['GET'])
    def get_suscriptions():
        suscripciones = Suscripcion.query.all()
        if not suscripciones:
            return jsonify({
                'success': False,
                'error': 'No se encontraron suscripciones'
            }), 404

        return jsonify({
            'success': True,
            'suscripciones': [suscripcion.serialize() for suscripcion in suscripciones]
        }), 200


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

