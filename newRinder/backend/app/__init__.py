# Libraries

from .models import db, Usuario, Perfil, Chat, Mensaje, Suscripcion, Compra, Like, setup_db, Pertenece
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
from flask_bcrypt import Bcrypt

import sys
import sys
import uuid
import json
from datetime import datetime
from flask_bcrypt import Bcrypt


# App

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    app.config['JWT_SECRET_KEY'] = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

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
        return response

    # Routes API

    # GET ------------------------------------------------------------------
    @app.route('/chats/<id>/mensajes', methods=['GET'])
    @jwt_required()
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

    @app.route('/usuarios/<correo>/chats', methods=['GET'])
    @jwt_required()
    def get_usuarios_chats(correo):
        user_id = get_jwt_identity()
        code = 200
        error_message = ""

        usuario = Usuario.query.filter_by(id_usuario=user_id).first()
        if not usuario:
            abort(404)

        if usuario.correo != correo:
            abort(401)

        id = usuario.id_usuario

        try:
            chats = Pertenece.query.filter_by(id_usuario=id).all()
            if not chats:
                code = 404
                error_message = "No se encontraron chats"
        except Exception as e:
            print(e)
            code = 500

        if code == 404:
            return jsonify({
                'success': False,
                'error': error_message
            }), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({
                'success': True,
                'chats': [chat.serialize() for chat in chats]
            }), code

    @app.route('/perfiles', methods=['GET'])
    def get_perfil():
        code = 200
        try:
            id = get_jwt_identity()

            if id:
                ids_likeados = (db.session.query(LikeaPerfil.id_usuario).filter(
                    LikeaPerfil.id_usuario == "mi id").subquery())
                perfiles = Perfil.query.filter(
                    Perfil.id_usuario.in_(ids_likeados)).all()
            else:
                perfiles = Perfil.query.all()

            if not perfiles:
                code = 404

        except Exception as e:
            print(e)
            code = 500

        if code == 404:
            return jsonify({
                'success': False,
                'error': 'No se encontraron perfiles'
            }), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({
                'success': True,
                'perfiles': [perfil.serialize() for perfil in perfiles]
            }), code

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
    @jwt_required()
    def get_compras():
        creadores = ['casurpiemelisante', 'giansegg', 'isabellaromero']
        if get_jwt_identity() not in creadores:
            return jsonify({
                'success': False,
                'error': 'No tiene permisos para ver las compras'
            }), 401

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

    @app.route('/usuarios/<id>/compras', methods=['GET'])
    @jwt_required()
    def get_compras_usuario(id):
        if get_jwt_identity() != id:
            abort(401)

        code = 200
        error_message = ""

        try:
            compras = Compra.query.filter_by(id_usuario=id).all()
            if not compras:
                code = 404
                error_message = "No se encontraron compras"
        except Exception as e:
            print(e)
            code = 500

        if code == 404:
            return jsonify({
                'success': False,
                'error': error_message
            }), code
        elif code != 200:
            abort(code)
        else:
            return jsonify({
                'success': True,
                'compras': [compra.serialize() for compra in compras]
            }), code

    # PATCH ----------------------------------------------------------------

    @app.route('/perfiles', methods=['PATCH'])
    @jwt_required()
    def patch_perfil():
        returned_code = 200
        list_errors = []
        try:
            id_usuario = get_jwt_identity()
            body = request.json
            Perfil = Perfil.query.filter_by(id_usuario=id_usuario).first()
            if Perfil:
                if 'nombre' in body:
                    nombre = body['nombre']
                    Perfil.nombre = nombre
                if 'apellido' in body:
                    apellido = body['apellido']
                    Perfil.apellido = apellido
                if 'descripcion' in body:
                    descripcion = body['descripcion']
                    Perfil.descripcion = descripcion
                if 'ruta_photo' in body:
                    ruta_photo = body['ruta_photo']
                    Perfil.ruta_photo = ruta_photo
                if 'ruta_network' in body:
                    ruta_network = body['ruta_network']
                    Perfil.ruta_network = ruta_network

                Perfil.modified_at = datetime.utcnow()
                db.session.commit()
            else:
                returned_code = 404
                list_errors.append('Perfil not found')

        except Exception as e:
            returned_code = 500
            list_errors.append(str(e))
        finally:
            if returned_code == 200:
                return jsonify({
                    'success': True,
                    'perfil': Perfil.serialize()
                }), returned_code
            else:
                return jsonify({
                    'success': False,
                    'errors': list_errors
                }), returned_code

    @app.route('/usuarios', methods=['PATCH'])
    @jwt_required()
    def patch_users():
        returned_code = 200
        list_errors = []
        try:
            id_usuario = get_jwt_identity()
            body = request.json
            usuario = Usuario.query.filter_by(id_usuario=id_usuario).first()

            if usuario:
                if 'correo' in body:
                    correo = body['correo']
                    usuario.correo = correo
                if 'contraseña' in body:
                    hashed_password = bcrypt.generate_password_hash(
                        body['contraseña']).decode('utf-8')
                    if not bcrypt.check_password_hash(usuario.contraseña, body['contraseña_actual']):
                        return jsonify({
                            'success': False,
                            'error': 'Contraseña actual incorrecta'
                        }), 401
                    else:
                        usuario.contraseña = hashed_password

                db.session.commit()
            else:
                returned_code = 404
                list_errors.append('Usuario no encontrado')

        except Exception as e:
            returned_code = 500
            list_errors.append(str(e))

        if returned_code == 200:
            return jsonify({
                'success': True,
                'usuario': usuario.serialize()
            }), returned_code
        else:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), returned_code

    @app.route('/compras', methods=['PATCH'])
    @jwt_required()
    def patch_compras():
        returned_code = 200
        list_errors = []
        try:
            id_usuario = get_jwt_identity()
            body = request.json
            compra = Compra.query.filter_by(id_usuario=id_usuario).first()

            if compra:
                if 'suscripcion' in body:
                    suscripcion = body['suscripcion']
                    compra.suscripcion = suscripcion
                if 'precio_compra' in body:
                    precio_compra = body['precio_compra']
                    compra.precio_compra = precio_compra

                db.session.commit()
            else:
                returned_code = 404
                list_errors.append(
                    'Compra no encontrada para el usuario actual')
                return jsonify({
                    'success': False,
                    'errors': list_errors
                }), returned_code

        except Exception as e:
            returned_code = 500
            list_errors.append(str(e))

        if returned_code == 200:
            return jsonify({
                'success': True,
                'compra': compra.serialize()
            }), returned_code
        else:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), returned_code

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
            if 'contraseña' not in body:
                list_errors.append('contraseña is required')
            else:
                contraseña = body['contraseña']

            if len(list_errors) > 0:
                returned_code = 400
            else:
                search_user = Usuario.query.filter_by(correo=correo).first()

                if search_user:
                    returned_code = 409
                else:
                    usuario = Usuario(correo, contraseña)
                    id_usuario = usuario.insert()

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating User', 'errors': list_errors}), returned_code
        elif returned_code == 409:
            return jsonify({"success": False, "message": 'User already exists'}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({
                'success': True,
                'message': 'User created',
                'id_usuario': id_usuario
            }), returned_code

    @app.route('/chats/<id>/mensajes', methods=['POST'])
    @jwt_required()
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
    @jwt_required()
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
                    suscripcion_search = Suscripcion.query.filter_by(
                        nombre=nombre).first()
                    if suscripcion_search:
                        returned_code = 409
                    else:
                        suscripcion = Suscripcion(nombre=nombre, precio=precio)
                        db.session.add(suscripcion)
                        db.session.commit()
                        returned_code = 201
            else:
                returned_code = 401

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Suscripcion', 'errors': list_errors}), returned_code
        elif returned_code == 409:
            return jsonify({"success": False, "message": 'Suscripcion already exists'}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({
                'success': True,
                'message': 'Suscripcion created',
                'suscripcion': suscripcion.serialize()
            }), returned_code

    @app.route('/chats', methods=['POST'])
    def post_chats():
        returned_code = 201
        try:
            # crear chat
            chat = Chat()
            db.session.add(chat)
            db.session.commit()
            id_chat = chat.id_chat

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        if returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({
                'success': True,
                'message': 'Chat created',
                'id_chat': id_chat
            }), returned_code

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

    @app.route('/usuarios/<id>', methods=['DELETE'])
    @jwt_required()
    def delete_users(id):
        list_errors = []
        returned_code = 200
        id_usuario = get_jwt_identity()

        if id_current_user != id:
            returned_code = 401
        else:
            try:
                usuario = Usuario.query.get(id_usuario)
                if usuario:
                    returned_code = usuario.delete()
                else:
                    returned_code = 404
            except Exception as e:
                print(sys.exc_info())
                db.session.rollback()
                returned_code = 500

        if returned_code == 404:
            return jsonify({"success": False, "message": 'Usuario no encontrado'}), returned_code
        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'message': 'Usuario eliminado exitosamente'}), returned_code

    @app.route('/suscripciones/<nombre>', methods=['DELETE'])
    @jwt_required()
    def delete_suscriptions():
        creadores = ['casurpiemelisante', 'giansegg', 'isabellaromero']
        id_usuario = get_jwt_identity()
        returned_code = 200

        if id_usuario not in creadores:
            abort(401)

        else:
            suscripcion = Suscripcion.query.filter_by(nombre=nombre).first()
            if suscripcion:
                db.session.delete(suscripcion)
                db.session.commit()
                returned_code = 200
            else:
                returned_code = 404

        if returned_code == 404:
            return jsonify({"success": False, "message": 'Suscripcion no encontrada'}), returned_code
        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'message': 'Suscripcion eliminada exitosamente'}), returned_code

    # LOGIN ----------------------------------------------------------------

    @app.route('/api/login', methods=['POST'])
    def login():
        returned_code = 200
        list_errors = []
        try:
            body = request.json
            if 'correo' not in body:
                list_errors.append('correo is required')
            else:
                correo = body['correo']
            if 'password' not in body:
                list_errors.append('password is required')
            else:
                password = body['password']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                usuario = Usuario.query.filter_by(correo=correo).first()

                if usuario and usuario.check_password(password):
                    access_token = create_access_token(
                        identity=usuario.id_usuario)
                    returned_code = 200
                else:
                    returned_code = 401
                    list_errors.append('Usuario o contraseña incorrectos')

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()

        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error logging in', 'errors': list_errors}), returned_code
        elif returned_code == 401:
            return jsonify({"success": False, "message": 'Error logging in', 'errors': list_errors}), returned_code

        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'message': 'Login successfully', 'access_token': access_token}), returned_code

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

    @app.errorhandler(409)
    def conflict(error):
        return jsonify({"success": False, "message": 'Conflict'}), 409

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"success": False, "message": 'Server error'}), 500

    @app.errorhandler(501)
    def not_implemented(error):
        return jsonify({"success": False, "message": 'Not implemented'}), 501

    return app
