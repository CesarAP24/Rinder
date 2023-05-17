# Rinder

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


# Librerias:

[Enlace al archivo de requerimientos](https://github.com/CesarAP24/Rinder/blob/AdvanceBE/requerimientos.txt)


## Commits:

El avance del proyecto se encuetra en las siguientes ramas:

main<br>
AdvanceFE -> Cesar e Isabella<br>
AdvanceBE -> Cesar y Gianpier<br>
  


## Funcionalidades de la app:
- Matchear <br>
	La app debe ser capaz de matchear de forma "inteligente" a los usuarios, mostrandoles primero los que más podrían encajar con ellos

- Interaccion <br>
	Los usuarios que matchean, pueden interatucar entre si.

- Posts(API Version)<br>
	La app tiene un sistema de posts que le permite al usuario compartir fotos, videos, comentarios o su vida en general. De este modo puede interactuar de mejor forma con la gente interesada en este.

- Monetización<br>
	El usuario puede pagar por una cuenta premium que le permita acceder a más funcionalidades, como por ejemplo, ver a los usuarios que le dieron like. Ver los usuarios que observan su perfil o tener likes ilimitados

	Es justo en este punto en el que recalcamos que los likes para una cuenta gratuita son limitados. Es decir, una cuenta gratuita podrá dar hasta 15 likes diarios.

- Tipos de planes
	- Gratuito
		Las cuentas gratuitas pueden dar de 10 a 20 likes diarios y tienen acceso a los posts de los usuarios que le dieron like. Sin embargo tienen anuncios presentes en la app.
	- Premium
		Los premium tieneen hasta 50 likes por día y a diferencia de los gratuitos estos no poseen anuncios.
	- Vip
		Los usuarios VIP pueden observar a los usuarios que le dieron like, tienen likes ilimitados y no poseen anuncios.

## Host:
localhost

## Puerto:
5432

# Manejo de errores HTTP: 

### Errores del servidor:

500 : Generalmente se refiere a un "Error interno del servidor"	<br> 
400 : Errores del cliente <br>
404 : Ruta no existente <br>
405 : Ruta, con un metodo no permitido <br>
200 : Respuesta exitosa <br>


## Como ejecutar el sistema :

1.- git clone https://github.com/CesarAP24/Rinder.git <br>
2.- pip install -r requerimientos.txt <br>
3.- correr el codigo app.py en la terminal <br> 

