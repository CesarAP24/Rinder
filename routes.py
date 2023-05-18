# IMPORTS ------------------------------------------------------------------------------------------------
# ========================================================================================================

# flask --------------------------------------------------------------------------------------------------

from flask import(
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    session,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

# libraries ----------------------------------------------------------------------------------------------

import uuid
from datetime import datetime
import json
import pandas as pd
from flask_bcrypt import Bcrypt
import os
import random

# CONFIGURATIONS -----------------------------------------------------------------------------------------

from app import *;




# ROUTES -------------------------------------------------------------------------------------------------
# ========================================================================================================


# Retorna el json del error con el codigo de error y el mensaje
def error(code):
    errors = {
        "400": "Solicitud incorrecta",
        "401": "No autorizado",
        "403": "Prohibido",
        "404": "404 no encontrado :(",
        "405": "Método no permitido",
        "-1": "Error desconocido"
    }
    messages = {
        "400": "La solicitud no se pudo entender por una sintaxis incorrecta.",
        "401": "No se ha autenticado o no se ha proporcionado una autorización válida.",
        "403": "No tiene permiso para acceder a este recurso.",
        "404": "El recurso solicitado no se encuentra en el servidor.",
        "405": "El método que se está intentando usar no está permitido en esta ruta.",
        "-1": "Lo sentimos, algo salió mal."
    }
    return render_template('error.html', error={"name":errors[code], "description":messages[code]}), int(code);


# Retorna un int con el permiso que tiene este usuario
def verificar_permisos(idUsuario):
    # -1 significa que no se pudo verificar
    # 0 significa que no tiene permisos
    # 1 significa que tiene permisos de usuario
    # 2 significa que tiene permisos de administrador
    
    return 1;


# MAIN ROUTE
# =============================================================================
@app.route('/')
def index():
    # verificar cookies
    if session.get('id_usuario'):
        # si: iniciar sesión
        return render_template('index.html')

    # de otro modo:
    return render_template('login.html') #redirigir al login page

# -----------------------------------------------------------------------------



# Login - Logout --------------------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # buscar usuario
        data = request.form;

        user = Usuario.query.filter_by(correo=data["email_login"]).first();

        if not(user):
            return jsonify({"success": False, "message": "Usuario no encontrado"}), 400;
        else:
            # verificar contraseña
            try:
                if bcrypt.check_password_hash(user.contraseña, data["password_login"]):
                    # iniciar sesión
                    session['id_usuario'] = user.id_usuario;
                    return jsonify({"success": True, "message": "Sesión iniciada"}), 200;
                else:
                    return jsonify({"success": False, "message": "Contraseña incorrecta"}), 400;

            except Exception as e:
                return jsonify({"success": False, "message": "Error desconocido, inicia sesión con otra cuenta"}), 500;

        return error("400");

    return error("405");



# registrar usuario ------------------------------------------------------------

@app.route('/register', methods=['POST'])
def register():
    session.clear(); # borrar session

    # obtener datos
    data = request.form;

    # verificar que no exista el usuario
    user = Usuario.query.filter_by(correo=data["email"]).first();

    if user: 
        return {"success": False, "message": "Correo ya registrado"}
    
    user = Usuario.query.filter_by(username=data["username"]).first();

    if user:
        return {"success": False, "message": "El username ya existe"}

    # hashear la contraseña

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8');


    # crear usuario
    id = str(uuid.uuid4());
    user = Usuario(
        id_usuario=id,
        username=data["username"],
        correo=data["email"],
        contraseña=hashed_password,
        active=True,
        likes_restantes=10
    );

    print(user)

    # crear perfil
    perfil = Perfil(
        username=data["username"],
        nombre=data["nombre"],
        apellido=data["apellido"],
        nacimiento=data["fecha_nacimiento"],
        edad=0,
        created_at=datetime.now(),
        modified_at=datetime.now()
        )

    print(perfil)


    # gurdar usuario y perfil

    db.session.add(user);
    db.session.add(perfil);
    db.session.commit();


    session['id_usuario'] = id;

    return redirect('/')




@app.route('/logout')
def logout():
    session.clear();
    return redirect('/')




@app.route('/mensajes/list', methods=['POST'])
def mensajes():
    # selecciona los chats donde aparece el usuario actual
    id_usuario = session.get('id_usuario'); 
    user_chats = Chat.query.filter_by(id_usuario=id_usuario).all();
    user_chats2 = Chat.query.filter_by(id_usuario2=id_usuario).all();
    chats = [];

    #guarda los chats en una lista
    for chat in user_chats:
        chats.append(chat.serialize());

    for chat in user_chats2:
        chats.append(chat.serialize());


    #serializa
    for chat in chats:
        id_other = chat["id_usuario2"] if chat["id_usuario2"] != id_usuario else chat["id_usuario"];
        otherUser = Usuario.query.filter_by(id_usuario=id_other).first();
        otherPerfil = Perfil.query.filter_by(username=otherUser.username).first();
        
        chat["otherUser"] = otherPerfil.serialize();
        chat["otherUser"]["other_id"] = otherUser.id_usuario;

        ultimo_mensajito = Mensaje.query.filter_by(id_mensaje = chat["id_mensaje"]).first();
        chat["lastMessage"] = ultimo_mensajito.serialize();





    return jsonify({'success': True, 'data': chats}), 200;


@app.route('/perfil', methods=['POST'])
def perfil():
    if request.method == 'POST':
        id = session.get('id_usuario'); 
        print(id);
        if not(id): return error("401"); # no se ha iniciado sesión

        user = Usuario.query.filter_by(id_usuario=id).first();
        if not(user): return error("404"); # no se encontró el usuario

        perfil = Perfil.query.filter_by(username=user.username).first();
        if not(perfil): return error("404"); # no se encontró el perfil


        # obtener datos
        data_out = perfil.serialize();
        data_out["id_user"] = session.get('id_usuario');
        return jsonify(data_out), 200;

    return error("405");



@app.route('/submit-photo', methods=['POST'])
def submit_photo():
    #checkear cookies
    if not(session.get('id_usuario')):
        return error("401");

    #obtener los datos de la imagen
    image = request.files['file-upload']
    folderName = os.getcwd()
    folderName = os.path.join(folderName, 'static', 'profilePhotos', session.get('id_usuario'))

    #crea el directorio para guardar la foto
    os.makedirs(folderName, exist_ok=True)


    image.save(os.path.join(folderName, image.filename))

    #guardar la imagen en la base de datos
    user = Usuario.query.filter_by(id_usuario=session.get('id_usuario')).first();
    perfil = Perfil.query.filter_by(username=user.username).first();
    print(perfil)
    perfil.ruta_photo = image.filename;
    db.session.commit();


    return jsonify({'success': True}), 200;


@app.route('/submit-profile', methods=['POST'])
def submit_profile():
    #checkear cookies
    if not(session.get('id_usuario')):
        return error("401");

    #obtener datos del perfil de tipo json
    #username, name, description
    try:
        data = request.get_json();
        user = Usuario.query.filter_by(id_usuario=session.get('id_usuario')).first();
        perfil = Perfil.query.filter_by(username=user.username).first();

        perfil.descripcion = data["description"];
        perfil.nombre = data["name"];


        user.username = None;
        db.session.commit();
        perfil.username = data["username"];
        db.session.commit();

        user.username = data["username"];
        db.session.commit();
    except Exception as e:
        print(e)
        return jsonify({'success': False}), 500;
    
    return jsonify({'success': False}), 200;






@app.route("/Users/match", methods=["GET"])
def get_Match():
    try:
        #obtener un usuario aleatorio:
        users = Usuario.query.all();
        user = random.choice(users);
        while user.id_usuario == session.get('id_usuario'):
            user = random.choice(users);

        perfil = Perfil.query.filter_by(username=user.username).first();

        out = perfil.serialize(); #funcion de la clase
        out["user_id"] = user.id_usuario;


        return jsonify({"success": True, "data": out}), 200;

    except Exception as e:
        print(e)
        return jsonify({"success": False}), 500;




@app.route("/Mensajes", methods=["GET", "POST"])
def Mensajes():
    if request.method == "POST":
        #obtener los datos
        id_usuario = session.get('id_usuario'); 
        data = request.get_json();
        chat = Chat.query.filter_by(id_chat = data["chat_id"]).first();
        
        if not(chat): return jsonify({"success": False}), 404;

        #crear el mensaje
        new_id_message = str(uuid.uuid4());
        new_message = Mensaje(id_mensaje=new_id_message, id_usuarioremitente=id_usuario, id_chat=data["chat_id"], id_mensajePadre=chat.id_mensaje, contenido=data["mensaje"]);
        
        db.session.add(new_message);
        db.session.commit();

        #actualizar el chat
        chat.id_mensaje = new_id_message;
        db.session.commit();
        
        return "{}", 200;
    elif request.method == "GET":
        data = request.args;
        id_mensajito = data["id_mensaje"];
        mensajes = [];
        for x in range(30):
            if id_mensajito:
                mensaje = Mensaje.query.filter_by(id_mensaje=id_mensajito).first();
                if mensaje:
                    mensajes.append(mensaje.serialize());
                    id_mensajito = mensaje.id_mensajePadre;
                else:
                    break;


        for x in range(len(mensajes)):
            if session.get('id_usuario') == mensajes[x]["id_usuarioremitente"]:
                mensajes[x]["propietario"] = 1;

            elif not(mensajes[x]["id_usuarioremitente"]):
                mensajes[x]["propietario"] = 0;

            else:
                mensajes[x]["propietario"] = -1;


        mensajes.reverse();
        return jsonify({"success": True, "data": mensajes}), 200;

    return render_template("Mensajes.html")



@app.route("/Users/match/check", methods=["POST"])
def check_match():
    #obtener payload
    id_usuario_likeado = request.get_json()["user_id"];
    id_usuario_likeador = session.get('id_usuario');

    #crear like
    like = Likea_Perfil(id_usuario_likeador, id_usuario_likeado, datetime.now());

    #verificar si hizo match, si existe un like de ese usuario hacia el 
    like_expected = Likea_Perfil.query.filter_by(id_usuario=id_usuario_likeado, id_usuario2=id_usuario_likeador).first();


    if like_expected:
        #si existe crear un chat con esa persona
        id_chat = str(uuid.uuid4());
        id_mensaje = str(uuid.uuid4());
        chat = Chat(id_usuario=id_usuario_likeador, id_usuario2=id_usuario_likeado, fecha=datetime.now(), id_chat=id_chat);
        server_message = Mensaje(fecha=datetime.now(), contenido="Has matcheado!", id_chat=id_chat, id_mensaje=id_mensaje);
        try:
            if Chat.query.filter_by(id_usuario=id_usuario_likeador, id_usuario2=id_usuario_likeado).first() or Chat.query.filter_by(id_usuario=id_usuario_likeado, id_usuario2=id_usuario_likeador).first():
                return jsonify({"success": False, "match": True}), 200;
            db.session.add(chat);
            db.session.add(server_message);
            db.session.commit();
            
            chat.id_mensaje = id_mensaje;
            db.session.commit();
            
        except Exception as e:
            print(e)
            db.session.rollback(); #si falla, hacer rollback
            return jsonify({"success": False, "message": "Ya se le dió like a este perfil"}), 500;
        
        return jsonify({"success": True, "match": True}), 200;

    else:
        db.session.add(like);
        db.session.commit();

    return jsonify({"success": False, "message": "Ya se le dió like a este perfil"}), 400;


    return jsonify({"success": True, "match": False}), 200;




#manejo de errores
@app.errorhandler(405)
def page_not_found(e):
    return error("405");

@app.errorhandler(404)
def page_not_found(e):
    return error("404");
