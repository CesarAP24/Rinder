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
Rinder es un servicio web de citas que utiliza el framework de desarrollo web Flask en Python, junto con una serie de librerías. Este servicio está diseñado para brindar una experiencia satisfactoria en las citas, permitiendo a los usuarios establecer conexiones e interacciones con otras personas de manera efectiva. Rinder ofrece un proceso más intuitivo y eficaz para encontrar personas altamente compatibles.

Además, Rinder utiliza Vue.js como su framework de frontend, lo que proporciona una interfaz de usuario dinámica y receptiva. Con Vue.js, los usuarios pueden disfrutar de una experiencia de navegación fluida y enriquecedora en Rinder. Además, Vue.js permite una gestión eficiente de los componentes de la interfaz de usuario, lo que contribuye a la escalabilidad y mantenibilidad del sistema.

Rinder también ha integrado el API de PayPal para ofrecer a los usuarios la posibilidad de adquirir suscripciones premium. A través del uso del API de PayPal, los usuarios pueden realizar pagos seguros y disfrutar de beneficios exclusivos al suscribirse a Rinder. Esta integración con PayPal proporciona una forma conveniente y confiable de acceder a características premium y mejorar la experiencia de citas en Rinder.
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

frontback2 -> backend <br>
frontVue -> Frontend

Componentes:
LoginForm.vue <br>
MatchCard.vue <br>
MessageBubbles.vue <br>
MessageInput.vue <br> 
MessageList.vue <br>
MessagesChats.vue <br>
PlanCard.vue <br>
ProfileContent.vue <br>
ProfileHeader.vue <br>
RegisterForm.vue <br>
SideBar.vue <br>
paypalButton.vue <br>
  

## Funcionalidades de la app:
- Matchear <br>
	La app debe ser capaz de matchear de forma "inteligente" a los usuarios, mostrandoles primero los que más podrían encajar con ellos

- Interaccion <br>
	Los usuarios que matchean, pueden interatucar entre si.

- Posts(API Version)<br>
	La app tiene un sistema de posts que le permite al usuario compartir fotos, videos, comentarios o su vida en general. De este modo puede interactuar de mejor forma con la gente interesada en este.

- Monetización<br>
	El usuario puede realizar donaciones, nosotros colocamos un monto minimo entonces esto nos ayudará a financiar el proyecto y realizar grandes mejoras

## Host:
localhost

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

1.- git clone https://github.com/CesarAP24/Rinder.git <br>
2.- pip install -r requerimientos.txt <br>
3.- correr el codigo app.py en la terminal <br> 
4.- Instalar las dependencias por parte del frontend 
5.- npm install 

![](C:\Users\cesar\Desktop\proectos%20universidad\Rinder\DIAGRAMA.PNG)
