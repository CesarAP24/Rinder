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

import sys
import uuid
import json
from datetime import datetime
from flask_bcrypt import Bcrypt
from datetime import timedelta


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
        create_default_data(app, db)

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
            chats = Chat.query.filter(Chat.id_chat.in_([chat.id_chat for chat in chats])).all()
            chats = [chat.serialize() for chat in chats]

            if not chats:
                code = 404
                error_message = "No se encontraron chats"
            else:
                #asignar la photo del chat que no sea la foto del usuario
                for chat in range(len(chats)):
                    #buscar usuarios que pertenecen al chat
                    usuarios = Pertenece.query.filter_by(id_chat=chats[chat]['id_chat']).all()
                    id_usuarios = [usuario.id_usuario for usuario in usuarios]
                    perfiles = Perfil.query.filter(Perfil.id_usuario.in_(id_usuarios)).all()

                    if len(usuarios) == 1:
                        chats[chat]['photo'] = perfiles[0].ruta_photo
                    else:
                        for perfil in perfiles:
                            if perfil.id_usuario != id:
                                chats[chat]['photo'] = perfil.ruta_photo
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
                'chats': chats
            }), code

    @app.route('/perfiles', methods=['GET'])
    @jwt_required()
    def get_perfil():
        code = 200
        try:
            id = get_jwt_identity()

            #usuario existe?
            usuario = Usuario.query.filter_by(id_usuario=id).first()
            if not usuario:
                abort(404)

            #buscar perfiles que el usuario no haya likeado
            likes = Like.query.filter_by(id_usuario=id).all()
            id_likes = [like.id_usuario_likeado for like in likes]
            perfiles = Perfil.query.filter(Perfil.id_usuario.notin_(id_likes)).all()

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


    @app.route('/usuarios/<correo>/compras', methods=['GET'])
    @jwt_required()
    def get_compras_usuario(correo):
        user = Usuario.query.filter_by(correo=correo).first()
        if not user:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario'
            }), 404
        else:
            id = user.id_usuario
        if get_jwt_identity() != id:
            abort(401)

        code = 200
        error_message = "";

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
    @app.route('/perfiles/<correo>', methods=['PATCH'])
    @jwt_required()
    def patch_perfil(correo):
        returned_code = 200
        list_errors = []
        search_user = Usuario.query.filter_by(correo=correo).first()
        if not(search_user):
            return jsonify({
                'success': False,
                'error': 'El usuario no existe'
            }), 404

        id_usuario = get_jwt_identity()
        
        if search_user.id_usuario != id_usuario:
            abort(401)

        try:
            body = request.get_json()

            profile = Perfil.query.filter_by(id_usuario=id_usuario).first()
            
            if profile:
                if 'nombre' in body:
                    nombre = body['nombre']
                    profile.nombre = nombre
                if 'apellido' in body:
                    apellido = body['apellido']
                    profile.apellido = apellido
                if 'descripcion' in body:
                    descripcion = body['descripcion']
                    profile.descripcion = descripcion
                if 'ruta_photo' in body:
                    ruta_photo = body['ruta_photo']
                    profile.ruta_photo = ruta_photo

                profile.modified_at = datetime.utcnow()
                db.session.commit()
            else:
                returned_code = 404
                list_errors.append('Perfil not found')

        except Exception as e:
            print(e)
            returned_code = 500


        if returned_code == 404:
            return jsonify({
                'success': False,
                'error': list_errors
            }), 404
        elif returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({
                'success': True,
                'message': 'Perfil actualizado exitosamente',
                'Perfil': profile.serialize()
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
                'correo': usuario.correo
            }), returned_code
        else:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), returned_code

    # @app.route('/compras', methods=['PATCH'])
    # @jwt_required()
    # def patch_compras():
    #     returned_code = 200
    #     list_errors = []
    #     try:
    #         id_usuario = get_jwt_identity()
    #         body = request.json
    #         compra = Compra.query.filter_by(id_usuario=id_usuario).first()

    #         if compra:
    #             if 'suscripcion' in body:
    #                 suscripcion = body['suscripcion']
    #                 compra.suscripcion = suscripcion
    #             if 'precio_compra' in body:
    #                 precio_compra = body['precio_compra']
    #                 compra.precio_compra = precio_compra

    #             db.session.commit()
    #         else:
    #             returned_code = 404
    #             list_errors.append(
    #                 'Compra no encontrada para el usuario actual')
    #             return jsonify({
    #                 'success': False,
    #                 'errors': list_errors
    #             }), returned_code

    #     except Exception as e:
    #         returned_code = 500
    #         list_errors.append(str(e))

    #     if returned_code == 200:
    #         return jsonify({
    #             'success': True,
    #             'compra': compra.serialize()
    #         }), returned_code
    #     else:
    #         return jsonify({
    #             'success': False,
    #             'errors': list_errors
    #         }), returned_code

    # POST -----------------------------------------------------------------

    @app.route('/usuarios', methods=['POST'])
    def post_users():
        returned_code = 201
        list_errors = []
        try:
            body = request.get_json()
            if 'correo' not in body:
                list_errors.append('correo is required')
            else:
                correo = body['correo']
            if 'contraseña' not in body:
                list_errors.append('contraseña is required')
            else:
                contraseña = body['contraseña']
            if 'nombre' not in body:
                list_errors.append('nombre is required')
            else:
                nombre = body['nombre']
            if 'apellido' not in body:
                list_errors.append('apellido is required')
            else:
                apellido = body['apellido']
            if 'nacimiento' not in body:
                list_errors.append('nacimiento is required')
            else:
                nacimiento = body['nacimiento']
            if 'genero' not in body:
                list_errors.append('genero is required')
            else:
                genero = body['genero']

            if len(list_errors) > 0:
                returned_code = 400
            else:
                search_user = Usuario.query.filter_by(correo=correo).first()

                if search_user:
                    returned_code = 409
                else:
                    usuario = Usuario(correo, contraseña)
                    id_usuario = usuario.insert()

                    perfil = Perfil(id_usuario=id_usuario, nombre=nombre, apellido=apellido, nacimiento=nacimiento, genero=genero)
                    db.session.add(perfil)
                    db.session.commit()


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
            body = request.get_json()
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
                currently_chat.cantidad_mensajes = currently_chat.cantidad_mensajes + 1
                db.session.commit()

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500

        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Mensaje', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({"success": True, "message": 'Mensaje created successfully', "mensaje": mensaje.serialize()})

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
                    suscripcion_search = Suscripcion.query.filter_by(nombre=nombre).first()
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
    @jwt_required()
    def post_chats():
        id_usuario = get_jwt_identity()
        returned_code = 201

        current_user = Usuario.query.filter_by(id_usuario=id_usuario).first()

        if not current_user:
            return jsonify({"success": False, "message": 'User does not exist'}), 404

        profile = Perfil.query.filter_by(id_usuario=id_usuario).first()
        chat_photo = profile.ruta_photo

        try:
            #crear chat
            chat = Chat();
            db.session.add(chat )
            db.session.commit()
            id_chat = chat.id_chat

            #crear participacion
            pertenece = Pertenece(id_usuario=id_usuario, id_chat=id_chat)
            db.session.add(pertenece)
            db.session.commit()

            #crear mensaje de administrador
            mensaje = Mensaje(id_usuario=id_usuario, id_chat=id_chat, contenido='Chat iniciado')
            chat.cantidad_mensajes = chat.cantidad_mensajes + 1
            db.session.add(mensaje)
            db.session.commit()

            chat.id_mensaje = mensaje.id_mensaje
            db.session.commit()


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

    @app.route('/chats/usuarios', methods=['POST'])
    @jwt_required()
    def post_chats_usuarios():
        #verificar que pertenesca al chat
        pass

    @app.route('/compras', methods=['POST'])
    @jwt_required()
    def post_compras():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            id_usuario = get_jwt_identity()
            #CHECKEAR que el usuario exista
            user = Usuario.query.filter_by(id_usuario=id_usuario).first()
            if not user:
                returned_code = 404
                list_errors.append('User does not exist')
            else:
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
        elif returned_code == 404:
            return jsonify({"success": False, "message": 'Error creating Compra0', 'errors': list_errors}), returned_code
        else:
            return jsonify({"success": True, 'message': 'Compra created successfully'}), returned_code

    @app.route('/likes', methods=['POST'])
    @jwt_required()
    def post_likes():
        returned_code = 201
        list_errors = []
        try:
            body = request.get_json()
            id_usuario = get_jwt_identity()
            if 'correo_likeado' not in body:
                list_errors.append('correo_likeado is required')
            else:
                correo_likeado = body['correo_likeado']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                usuario_likeado = Usuario.query.filter_by(correo=correo_likeado).first()
                if usuario_likeado:
                    id_usuario_likeado = usuario_likeado.id_usuario
                    like = Like(id_usuario=id_usuario,
                                id_usuario_likeado=id_usuario_likeado)
                    db.session.add(like)
                    db.session.commit()
                else:
                    returned_code = 404
                    list_errors.append('Users that you are trying to like does not exist')

        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            returned_code = 500
        finally:
            db.session.close()
        if returned_code == 400:
            return jsonify({"success": False, "message": 'Error creating Like', 'errors': list_errors}), returned_code
        elif returned_code == 404:
            return jsonify({"success": False, "message": 'Error creating Like', 'errors': list_errors}), returned_code
        elif returned_code != 201:
            abort(returned_code)
        else:
            return jsonify({"success": True, 'message': 'Like created successfully'}), returned_code

    # DELETE --------------------------------------------------------------

    @app.route('/usuarios/<correo>', methods=['DELETE'])
    @jwt_required()
    def delete_users(correo):
        list_errors = []
        returned_code = 200
        id_usuario = get_jwt_identity()

        usuario = Usuario.query.filter_by(correo=correo).first()

        if not(usuario):
            returned_code = 404
        elif usuario.id_usuario != id_usuario:
            returned_code = 401
        else:
            try:
                returned_code = usuario.delete()
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
            if 'contraseña' not in body:
                list_errors.append('contraseña is required')
            else:
                password = body['contraseña']
            if len(list_errors) > 0:
                returned_code = 400
            else:
                usuario = Usuario.query.filter_by(correo=correo).first()

                if usuario and usuario.check_password(password):
                    #codigo de acceso de 30 dias
                    access_token = create_access_token(identity=usuario.id_usuario, expires_delta=timedelta(days=30))
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
