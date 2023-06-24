# Rutas, refactorización
---

### Necesidades

Vamos a listar las necesidades como CRUDs y modelos que usa Rinder.

## Actual:

### Rutas actuales:

- ('/')
- ('/login', methods=['POST'])
- ('/register', methods=['POST'])
- ('/logout')
- ('/mensajes/list', methods=['POST'])
- ('/perfil', methods=['POST'])
- ('/submit-photo', methods=['POST'])
- ('/submit-profile', methods=['POST'])
- ("/Users/match", methods=["GET"])
- ("/Mensajes", methods=["GET", "POST"])
- ("/Users/match/check", methods=["POST"])


Sin embargo, en la segunda parte del curso vimos que debemos enfocar nuestras aplicaciones para separar lo máximo posible el front del back. Por ende desarrollaremos una API que siga los estándares REST.


### Modelos Actuales:


- Usuario(id_usuario, username, correo, contraseña, active, likes_restantes)

- Perfil(username, nombre, apellido, nacimiento, edad, genero, descripcion, ruta_photo, created_at, modified_at)

- Publicacion(id_publicacion, id_usuario, contenido, modified_at, created_at, cantidad_likes)
	- Post(id_publicacion)
	- Comentario(id_publicacion, id_publicacion2)

- Chat(id_chat, id_usuario, id_usuario2, id_mensaje, fecha)
	- Mensaje(id_mensaje, id_usuarioremitente, id_chat, id_mensajePadre, fecha, contenido, state, formato)

- Suscripcion(nombre, precio, created, modified, day_duration)

- Likea_Perfil(id_usuario, id_usuario2, fdfrfecha)

- Likea_Publicacion(id_usuario, id_usuario2, id_publicacion, fecha)

- Compra(id_compra, id_usuario, nombre_suscripcion, fecha, precio_compra)


## Futuro:

Para establecer el futuro de Rinder debemos establecer unos nuevos modelos que se ajusten a las necesidades de la aplicación.

### Modelos Futuros:

- 

### Rutas Futuras:

Las rutas futuras deben ser correspondientes a una REST API, por ende, serán las siguientes:

- ('/')
- ('/login', methods=['POST'])
- ('/Usuarios', methods=['POST', 'GET', 'PATCH', 'DELETE'])
- ('/Perfiles', methods=['POST', 'GET', 'PATCH', 'DELETE'])
- ('/Publicaciones', methods=['POST', 'GET', 'PATCH', 'DELETE'])
- ('/Chats', methods=['POST', 'GET', 'PATCH', 'DELETE'])
- ('/Mensajes', methods=['POST', 'GET', 'PATCH', 'DELETE'])
- ('/Suscripciones', methods=['POST', 'GET', 'PATCH', 'DELETE'])