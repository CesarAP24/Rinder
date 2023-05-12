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
        "404": "Página no encontrada",
        "405": "Método no permitido",
    }
    messages = {
        "400": "La solicitud no se pudo entender por una sintaxis incorrecta.",
        "401": "No se ha autenticado o no se ha proporcionado una autorización válida.",
        "403": "No tiene permiso para acceder a este recurso.",
        "404": "El recurso solicitado no se encuentra en el servidor.",
        "405": "El método que se está intentando usar no está permitido en esta ruta.",
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
    print(session.get('id_usuario'))
    if session.get('id_usuario'): 
        # si: iniciar sesión
        return render_template('index.html')

    # de otro modo:
    return render_template('login.html') #redirigir al login page

# -----------------------------------------------------------------------------



# Login - Logout --------------------------------------------------------------

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # buscar usuario
        data = request.form;

        user = Usuario.query.filter_by(correo=data["email_login"]).first();

        if not(user):
            return {"success": False, "message": "Usuario no encontrado"}
        else:
            if user.contraseña == data['password_login']:
                # iniciar sesión
                session['id_usuario'] = user.id_usuario;
                return {"success": True, "message": "Sesión iniciada"}
            else:
                return {"success": False, "message": "Contraseña incorrecta"}

        return {"success": False, "message": "Error desconocido"}

    return redirect('/')



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


    # crear usuario
    id = str(uuid.uuid4());
    user = Usuario(
        id_usuario=id,
        username=data["username"],
        correo=data["email"],
        contraseña=data["password"],
        active=True,
        likes_restantes=10
    );

    session['id_usuario'] = id;

    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
