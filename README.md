# Rinder 2.0.0

<p align="center">
  <img src="https://github.com/CesarAP24/Rinder/raw/AdvanceBE/static/images/logofucsia.PNG" alt="Logo" width="30%">
</p>

## Integrantes:

- Gianpier Segovia
- César Perales
- Isabella Romero

## Descripción del proyecto:

<p align="justify">
Rinder es un servicio web de citas que utiliza el framework de desarrollo web Flask en Python, junto con una serie de librerías, entre las cuales destaca TensorFlow. Este servicio está diseñado para brindar una experiencia satisfactoria en las citas, utilizando redes neuronales para el aprendizaje automático. Rinder ayuda a los usuarios a establecer conexiones e interacciones con otras personas. Rinder ofrece un proceso más intuitivo y eficaz para encontrar personas altamente compatibles, aprovechando las capacidades de procesamiento y análisis de datos de la librería TensorFlow.
</p>

## Objetivos/Misión/Visión:

Misión:

<p align="justify">
La misión de Rinder como servicio es brindar una plataforma de citas en tiempo real que sea innovadora y eficiente, creando funcionalidades fuera de lo tradicional. El entorno de Rinder es seguro para los usuarios, permitiéndoles descubrir y conocer nuevas personas con las cuales son compatibles mediante el uso de redes neuronales. El objetivo de Rinder es facilitar a los usuarios a encontrar la felicidad a través de sus relaciones con otros usuarios en Rinder.
</p>

Visión

<p align="justify">
La visión de Rinder es convertirse en líderes dentro de la industria de citas en tiempo real, reconocidos por la seguridad que brindan a sus usuarios, la confiabilidad de su información personal y su capacidad para proporcionar conexiones auténticas. Rinder aspira a ser la plataforma de preferencia para aquellas personas que buscan establecer relaciones significativas.
</p>

## Composición:

Rinder se compone de 2 partes principales: Restful API y Frontend.

### Restful API:

La API de Rinder está desarrollada en Flask, un framework de desarrollo web en Python. La API está compuesta por 3 partes principales: el servidor, el modelo y la base de datos.

#### Modelos:

- `Perfil(id_usuario : PK FK, nombre, apellido, nacimiento, edad, genero, descripcion, ruta_photo)`
  
    Guarda todo lo referente a la información del usuario, como su nombre, edad, género, preferencias, etc.

- `Usuario(id_usuario : PK, correo, contraseña)`. 
  
    Guarda la información de la cuenta del usuario, como su correo electrónico, contraseña y el perfil asociado. El objetivo de tener dos modelos separados es para mantener la información de la cuenta del usuario separada de su información personal.

- `Publicación(id_publicacion : PK, id_usuario : FK, ruta_html)`. 
  
    Guarda la información de las publicaciones de los usuarios, como su contenido, fecha de publicación, etc. Una publicación puede ser un comentario o una foto.
  
  - `Comentario(id_publicacion : PK FK, id_publicacion2 : FK)`. 
    
      Un comentario es una publicación que tiene ascociada otra publicación, por lo que un usuario puede comentar una publicación y tambien responder a comentarios.
  
  - `Post(id_publicacion: PK FK)`. 
    
      Una Post es una publicación que no tiene asociada otra publicación, por lo que un usuario puede publicar una foto o un comentario.

- `Mensaje(id_mensaje : PK, id_usuario : FK, id_chat : FK, id_mensajePadre : FK)`. 
  
    Guarda la información de los mensajes enviados entre dos usuarios, como su contenido, fecha de envío, etc. Los mensajes tienen guardado el mensaje que va arriba de ellos, por lo que un mensaje puede ser una respuesta a otro mensaje y por tanto se puede cargar una conversación completa de forma recursiva.

- `Chat(id_chat : PK, fecha, nombre)`. 
  
    Guarda la información de los chats entre dos usuarios, como la fecha de creación, los usuarios que participan en el chat, etc.

- `EstaEnChat(id_usuario : PK FK, id_chat : PK FK)`. 
  
    Relaciona los usuarios con los chats en los que participan. Por tanto un chat puede tener varios usuarios. Sin embargo, si un chat no tiene nombre tomará el nombre de los usuarios dentro del chat sin incluir al usuario que está haciendo la consulta.

- `LikeaPerfil(id_usuario : PK FK, id_usuarioLikeado : PK FK)`. 
  
    Guarda la información de los likes que un usuario le da a un perfil, como la fecha en la que se dio el like.

- `LikeaPublicacion(id_usuario : PK FK, id_Publicacion : PK FK)`. 
  
    Guarda la información de los likes que un usuario le da a una publicación, como la fecha en la que se dio el like.

### Frontend:

Diagrama de componentes:

![](C:\Users\cesar\Desktop\proectos%20universidad\Rinder\DIAGRAMA.PNG)
