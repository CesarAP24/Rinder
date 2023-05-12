# IMPORTS ------------------------------------------------------------------------------------------------
# ========================================================================================================

# flask --------------------------------------------------------------------------------------------------

from flask import(
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey

# libraries ----------------------------------------------------------------------------------------------

import uuid
from datetime import datetime

# CONFIGURATIONS -----------------------------------------------------------------------------------------

from app import app





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
    return render_template('index.html')

# -----------------------------------------------------------------------------

# USUARIO
# =============================================================================

@app.route('/Usuarios', methods=['POST', 'GET'])
def Usuarios():
    # permisos
    if request.method == 'POST':
        # Crea un nuevo usuario
        return (jsonify({'error': 'Método no implementado'}), 501);

    elif request.method == 'GET':
        # Devolver todos los ids de los usuarios existentes
        return (jsonify({'message': 'Método no implementado'}), 501);

    elif request.method == 'PATCH':
        # modificar a algunos usuarios
        return (jsonify({'message': 'Método no implementado'}), 501);

    elif request.method == 'DELETE':
        # ELimina TODOS los usuarios
        return (jsonify({'message': 'Método no implementado'}), 501);

    else:
        return error(405);


@app.route('/Usuarios/<id>', methods=['GET', 'DELETE', 'PATCH'])
def Usuarios_id(id):
    # permisos
    if request.method == 'GET':
        # devolver el usuario con id
        return (jsonify({'message': 'Método no implementado'}), 501);
    elif request.method == 'DELETE':
        # elimina al usuario con id y su perfil
        return (jsonify({'message': 'Método no implementado'}), 501);
    elif request.method == 'PATCH':
        # modifica el usuario con id
        return (jsonify({'message': 'Método no implementado'}), 501);
    else:
        # metodo no permitido
        return error(405);


@app.route('/Usuarios/<id>/Perfiles', methods=['GET', 'PATCH'])
def Usuarios_id_perfil(id):
    # permisos
    if request.method == 'GET':
        # devolver el perfil
        pass
    elif request.method == 'PATCH':
        # MODIFICAR VALORES DEL PERFIL
        pass
    else:
        # metodo no permitido
        return error(405);


@app.route('/Usuarios/Perfiles', methods=['GET', 'PATCH'])
def Usuarios_perfiles():
    # permisos
    if request.method == 'GET':
        #devolver todos los perfiles
        pass
    elif request.method == 'PATCH':
        #modificar un perfil
        pass
    else:
        #metodo no permitido
        return error(405);


@app.route('/Usuarios/id/Mensajes', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Usuarios_id_mensajes(id):
    # permisos
    if request.method == 'GET':
        # devolver todos los mensajes de id
        pass
    elif request.method == 'POST':
        # crear un nuevo mensaje
        pass
    elif request.method == 'PATCH':
        # modificar un mensaje
        pass
    elif request.method == 'DELETE':
        # eliminar un mensaje
        pass
    else:
        # metodo no permitido
        return error(405);

@app.route('/Usuarios/id/Posts', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Usuarios_id_posts(id):
    # permisos
    if request.method == 'GET':
        # devolver todos los posts del usuario con id
        pass
    elif request.method == 'POST':
        # crear un nuevo post para el usuario con id
        pass
    elif request.method == 'PATCH':
        # modificar un post del usuario con id
        pass
    elif request.method == 'DELETE':
        # eliminar un post del usuario con id
        pass
    else:
        # metodo no permitido
        return error(405);

@app.route('/Usuarios/id/Suscripciones', methods=['GET', 'PATCH'])
def Usuarios_id_suscripciones(id):
    # permisos
    if request.method == 'GET':
        # devolver todas las suscripciones del usuario con id
        pass
    elif request.method == 'PATCH':
        # modificar una suscripcion del usuario con id
        pass
    else:
        # metodo no permitido
        return error(405);


@app.route('/Usuarios/Suscripciones', methods=['GET', 'PATCH'])
def Usuarios_suscripciones():
    # permisos
    if request.method == 'GET':
        # devolver todas las suscripciones de todos los usuarios
        pass
    elif request.method == 'PATCH':
        # modificar una suscripcion
        pass
    else:
        # metodo no permitido
        return error(405);


@app.route('/Usuarios/id/Comentarios', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Usuarios_id_comentarios(id):
    # permisos
    if request.method == 'GET':
        # devolver todos los comentarios del usuario con id
        pass
    elif request.method == 'POST':
        # crear un nuevo comentario para el usuario con id
        pass
    elif request.method == 'PATCH':
        # modificar los comentarios del usuario con id
        pass
    elif request.method == 'DELETE':
        # elimina TODOs los comentarios del usuario con id
        pass
    else:
        # metodo no permitido
        return error(405);

# -----------------------------------------------------------------------------






# SUSCRIPCIONES
# =============================================================================


@app.route('/Suscripciones', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Suscripciones():
    # permisos
    if request.method == 'GET':
        # devolver todas las suscripciones
        pass
    elif request.method == 'POST':
        # crear una nueva suscripcion
        pass
    elif request.method == 'PATCH':
        # modificar una suscripcion
        pass
    elif request.method == 'DELETE':
        # eliminar todas las sucripciones menos la gratuita
        pass
    else:
        # metodo no permitido
        return error(405);


@app.route('/Suscripciones/<nombre>', methods=['GET', 'DELETE', 'PATCH'])
def Suscripciones_nombre(nombre):
    # permisos
    if request.method == 'GET':
        # devolver la suscripcion con nombre
        pass
    elif request.method == 'DELETE':
        # eliminar la suscripcion con nombre
        pass
    elif request.method == 'PATCH':
        # modificar la suscripcion con nombre
        pass
    else:
        # metodo no permitido
        return error(405);

# -----------------------------------------------------------------------------



# POSTS
# =============================================================================

@app.route('/Posts', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Posts():
    # permisos
    if request.method == 'GET':
        # devolver todos los posts
        pass
    elif request.method == 'POST':
        # crear un nuevo post
        pass
    elif request.method == 'PATCH':
        # modificar un post
        pass
    elif request.method == 'DELETE':
        # eliminar todos los posts
        pass
    else:
        # metodo no permitido
        return error(405);

@app.route('/Posts/<id>', methods=['GET', 'DELETE', 'PATCH'])
def Posts_id(id):
    # permisos
    if request.method == 'GET':
        # devolver el post con id
        pass
    elif request.method == 'DELETE':
        # eliminar el post con id
        pass
    elif request.method == 'PATCH':
        # modificar el post con id
        pass
    else:
        # metodo no permitido
        return error(405);

@app.route('/Posts/<id>/Comentarios', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Posts_id_comentarios(id):
    # permisos
    if request.method == 'GET':
        # devolver todos los comentarios del post con id
        pass
    elif request.method == 'POST':
        # crear un nuevo comentario para el post con id
        pass
    elif request.method == 'PATCH':
        # modificar un comentario del post con id
        pass
    elif request.method == 'DELETE':
        # eliminar todos los comentarios del post con id
        pass
    else:
        # metodo no permitido
        return error(405);

# -----------------------------------------------------------------------------



# COMENTARIOS
# =============================================================================

@app.route('/Comentarios', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def Comentarios():
    # permisos
    if request.method == 'GET':
        # devolver todos los comentarios
        pass
    elif request.method == 'POST':
        # crear un nuevo comentario
        pass
    elif request.method == 'PATCH':
        # modificar un comentario
        pass
    elif request.method == 'DELETE':
        # eliminar TODOS los comentarios EXISTENTES
        pass
    else:
        # metodo no permitido
        return error(405);


@app.route('/Comentarios/<id>', methods=['GET', 'DELETE', 'PATCH'])
def Comentarios_id(id):
    # permisos
    if request.method == 'GET':
        # devolver el comentario con id
        pass
    elif request.method == 'DELETE':
        # eliminar el comentario con id
        pass
    elif request.method == 'PATCH':
        # modificar el comentario con id
        pass
    else:
        # metodo no permitido
        return error(405);