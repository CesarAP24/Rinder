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
from flask_bcrypt import Bcrypt

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




@app.route('/mensajes/list', methods=['GET'])
def mensajes():
    id_usuario = request.get['id_usuario']
    mensajes = db.session.query(Mensaje.id_usuarioremitente, Mensaje.id_usuariodestinatario, Mensaje.id_mensaje) \
        .filter((Mensaje.id_usuarioremitente == id_usuario) | (Mensaje.id_usuariodestinatario == id_usuario)) \
        .group_by(Mensaje.id_usuarioremitente, Mensaje.id_usuariodestinatario) \
        .order_by(db.func.MAX(Mensaje.fecha).desc()) \
        .all()

    resultado = []
    return jsonify({'success': True, 'data': resultado}), 200


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

        return jsonify(perfil.serialize()), 200;

    return error("405");





















































@app.route("/Mensajes", methods=["GET", "POST"])
def Mensajes():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        data = request.args;
        user_id = data["id_usuario"];

        pass

    return render_template("Mensajes.html")


#manejo de errores
@app.errorhandler(405)
def page_not_found(e):
    return error("405");

@app.errorhandler(404)
def page_not_found(e):
    return error("404");