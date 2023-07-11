# Libraries

from .models import db, Usuario, Perfil, Chat, Mensaje, Suscripcion, Compra, Like
from flask_cors import CORS
from .utilities import *

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    abort,
)

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from flask_bcrypt import Bcrypt

import sys
import uuid
import json
from datetime import datetime
from flask_bcrypt import Bcrypt


# App

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    app.config['JWT_SECRET_KEY'] = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response

    # Routes API

    # GET ------------------------------------------------------------------
    @app.route('/chats/<id>/mensajes', methods=['GET'])
    @jwt_required
    def get_mensajes(id):
        chat = Chat.query.filter_by(id_chat=id).first()
        user_id = get_jwt_identity()

        # checkear si el usuario participa en el chat
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
        compras = Compra.query.all()
        if not compras:
            return jsonify({
                'success': False,
                'error': 'No se encontraron compras'
            }), 404
        return jsonify({
            'success': True,
            'compras': [compra.serialize() for compra in compras]
        }), 200

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
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if 'correo' not in body:
                list_errors.append('correo is required')
            else:
                correo = body['correo']
                if Usuario.query.filter_by(correo=correo).first():
                    list_errors.append('correo already exists')
            if 'contraseña' not in body:
                list_errors.append('contraseña is required')
            else:
                hashed_password = bcrypt.generate_password_hash(
                    body['contraseña']).decode('utf-8')
                contraseña = hashed_password

            if len(list_errors) > 0:
                returned_code = 400
            else:
                id_usuario = str(uuid.uuid4())
                usuario = Usuario(id_usuario=id_usuario,
                                  correo=correo, contraseña=contraseña)
                db.session.add(usuario)
                db.session.commit()

                return jsonify({
                    "success": True,
                    "message": "Usuario creado exitosamente",
                    "usuario": usuario.serialize()
                }), returned_code
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating User', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'User created successfully'}), returned_code

    @app.route('/chats/<id>/mensajes', methods=['POST'])
    @jwt_required
    def post_mensajes(id):
        id_usuario = get_jwt_identity()
        id_chat = id
        id_mensajePadre = None
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            currently_chat = Chat.query.filter_by(id_chat=id_chat).first()
            id_last_mensaje = currently_chat.id_mensaje
            if not currently_chat:
                list_errors.append('Chat does not exist')
            if 'contenido' not in body:
                list_errors.append('contenido is required')
            else:
                contenido = body['contenido']
            if len(list_errors) > 0:
                returned_code = 400

            else:
                id_mensaje = str(uuid.uuid4())
                mensaje = Mensaje(id_mensaje=id_mensaje, id_usuario=id_usuario,
                                  id_chat=id_chat, id_mensajePadre=id_last_mensaje, contenido=contenido)
                db.session.add(mensaje)
                db.session.commit()
                currently_chat.id_mensaje = id_mensaje
                db.session.commit()

                return jsonify({
                    "success": True,
                    "message": "Mensaje creado exitosamente",
                    "mensaje": mensaje.serialize()
                }), returned_code
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Mensaje', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Mensaje created successfully'}), returned_code

    @app.route('/suscripciones', methods=['POST'])
    @jwt_required
    def post_suscriptions():
        creadores = ['casurpiemelisante', 'giansegg', 'isabellaromero']
        id_usuario = get_jwt_identity()
        returned_code = 201
        list_errors = []
        try:
            body = request.json

            if id_usuario in creadores:
                if 'nombre' not in body:
                    list_errors.append('nombre is required')
                else:
                    nombre = body['nombre']
                if 'precio' not in body:
                    list_errors.append('precio is required')
                else:
                    precio = body['precio']

                if len(list_errors) > 0:
                    returned_code = 400
                else:
                    suscripcion = Suscripcion(nombre=nombre, precio=precio)
                    db.session.add(suscripcion)
                    db.session.commit()

                    return jsonify({
                        "success": True,
                        "message": "Suscripcion creada exitosamente",
                        "suscripcion": suscripcion.serialize()
                    }), returned_code
            else:
                return jsonify({"success": False, "message": 'No tienes permiso para crear suscripciones'}), 401

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Suscripcion', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Suscripcion created successfully'}), returned_code

    @app.route('/chats', methods=['POST'])
    def post_compras():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if 'id_mensaje' not in body:
                list_errors.append('The chat is empty')
            else:
                id_mensaje = body['id_mensaje']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                chat = Chat(id_mensaje=id_mensaje)
                db.session.add(chat)
                db.session.commit()

                return jsonify({
                    "success": True,
                    "message": "Chat creado exitosamente",
                    "chat": chat.serialize()
                }), returned_code
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Chat', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Chat created successfully'}), returned_code

    @app.route('/compras', methods=['POST'])
    def post_compras():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            id_usuario = get_jwt_identity()
            if 'suscripcion' not in body:
                list_errors.append('suscripcion is required')
            else:
                suscripcion = body['suscripcion']
            if 'precio_compra' not in body:
                list_errors.append('precio_compra is required')
            else:
                precio_compra = body['precio_compra']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                compra = Compra(
                    id_usuario=id_usuario, suscripcion=suscripcion, precio_compra=precio_compra)
                db.session.add(compra)
                db.session.commit()

                return jsonify({
                    "success": True,
                    "message": "Compra creada exitosamente",
                    "compra": compra.serialize()
                }), returned_code
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Compra', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Compra created successfully'}), returned_code

    @app.route('/likes', methods=['POST'])
    def post_likes():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            id_usuario = get_jwt_identity()
            if 'id_usuario_likeado' not in body:
                list_errors.append('id_usuario_likeado is required')
            else:
                id_usuario_likeado = body['id_usuario_likeado']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                like = Like(id_usuario=id_usuario,
                            id_usuario_likeado=id_usuario_likeado)
                db.session.add(like)
                db.session.commit()

                return jsonify({
                    "success": True,
                    "message": "Like creado exitosamente",
                    "like": like.serialize()
                }), returned_code
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Like', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Like created successfully'}), returned_code

    # DELETE ---------------------------------------------------------------

    @app.route('/usuarios', methods=['DELETE'])
    def delete_users():
        list_errors = []
        returned_code = 200
        try:
            id_usuario = get_jwt_identity()
            usuario = Usuario.query.get(id_usuario)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return jsonify({
                    "success": True,
                    "message": "Usuario eliminado exitosamente"
                }), returned_code
            else:
                return jsonify({"success": False, "message": 'Usuario no encontrado'}), 404
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error deleting Usuario', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Usuario deleted successfully'}), returned_code

    @app.route('/suscripciones', methods=['DELETE'])
    def delete_suscriptions():
        creadores = ['casurpiemelisante', 'giansegg', 'isabellaromero']
        id_usuario = get_jwt_identity()
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if id_usuario not in creadores:
                list_errors.append('permiso denegado')
            else:
                if 'nombre' not in body:
                    list_errors.append('nombre is required')
                else:
                    nombre = body['nombre']
                if len(list_errors) > 0:
                    returned_code = 400
                else:
                    suscripcion = Suscripcion.query.get(nombre)
                    if suscripcion:
                        db.session.delete(suscripcion)
                        db.session.commit()
                        return jsonify({
                            "success": True,
                            "message": "Suscripcion eliminada exitosamente"
                        }), returned_code
                    else:
                        return jsonify({"success": False, "message": 'Suscripcion no encontrada'}), 404
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error deleting Suscripcion', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Suscripcion deleted successfully'}), returned_code

    # LOGIN ----------------------------------------------------------------

    @app.route('/api/login', methods=['POST'])
    def login():
        abort(501)

    # HANDLE ERROR ---------------------------------------------------------

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": 'Resource not found'}), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"success": False, "message": 'Unauthorized'}), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "message": 'Bad request'}), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({"success": False, "message": 'Method not allowed'}), 405

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({"success": False, "message": 'Forbidden'}), 403

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"success": False, "message": 'Server error'}), 500

    @app.errorhandler(501)
    def not_implemented(error):
        return jsonify({"success": False, "message": 'Not implemented'}), 501

    return app
