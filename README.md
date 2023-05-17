# Rinder

<p align="center">
  <img src="https://github.com/CesarAP24/Rinder/raw/AdvanceBE/static/images/logofucsia.PNG" alt="Logo" width="30%">
</p>


## Integrantes:
- Gianpier Segovia
- César Perales
- Isabella Romero

## Descripcion del proyecto:

<p align="justify">
Rinder es un servicio web de citas que utiliza el framework de desarrollo web Flask en Python, junto con una serie de librerías, entre las cuales destaca TensorFlow. Este servicio está diseñado para brindar una experiencia satisfactoria en las citas, utilizando redes neuronales para el aprendizaje automático. Rinder ayuda a los usuarios a establecer conexiones e interacciones con otras personas. Rinder ofrece un proceso más intuitivo y eficaz para encontrar personas altamente compatibles, aprovechando las capacidades de procesamiento y análisis de datos de la librería TensorFlow.
</p>


## Objetivos/Misión/Visión


Misión:
<p align="justify">
La misión de Rinder como servicio es brindar una plataforma de citas en tiempo real que sea innovadora y eficiente, creando funcionalidades fuera de lo tradicional. El entorno de Rinder es seguro para los usuarios, permitiéndoles descubrir y conocer nuevas personas con las cuales son compatibles mediante el uso de redes neuronales. El objetivo de Rinder es facilitar a los usuarios a encontrar la felicidad a través de sus relaciones con otros usuarios en Rinder.
</p>

Visión

<p align="justify">
La visión de Rinder es convertirse en líderes dentro de la industria de citas en tiempo real, reconocidos por la seguridad que brindan a sus usuarios, la confiabilidad de su información personal y su capacidad para proporcionar conexiones auténticas. Rinder aspira a ser la plataforma de preferencia para aquellas personas que buscan establecer relaciones significativas.
</p>


# Librerias:

absl-py==1.4.0
alembic==1.10.4
astunparse==1.6.3
blinker==1.6.2
cachetools==5.3.0
certifi==2023.5.7
charset-normalizer==3.1.0 <br>
click==8.1.3
Flask==2.3.2
Flask-Migrate==4.0.4
Flask-SQLAlchemy==3.0.3
flatbuffers==23.5.9
gast==0.4.0
google-auth==2.18.0
google-auth-oauthlib==1.0.0 <br>
google-pasta==0.2.0
greenlet==2.0.2
grpcio==1.54.2
h5py==3.8.0
idna==3.4 
itsdangerous==2.1.2
jax==0.4.10
Jinja2==3.1.2
keras==2.12.0 <br>
libclang==16.0.0
Mako==1.2.4
Markdown==3.4.3
MarkupSafe==2.1.2
ml-dtypes==0.1.0
numpy==1.23.5
oauthlib==3.2.2
opt-einsum==3.3.0<br>
packaging==23.1
pandas==2.0.1
protobuf==4.23.0
psycopg2-binary==2.9.1
pyasn1==0.5.0
pyasn1-modules==0.3.0
pyscopg2==66.0.2
python-dateutil==2.8.2 <br>
pytz==2023.3
requests==2.30.0
requests-oauthlib==1.3.1
rsa==4.9
scipy==1.10.1
six==1.16.0 <br>
SQLAlchemy==2.0.12
tensorboard==2.12.3
tensorboard-data-server==0.7.0
tensorflow==2.12.0
tensorflow-estimator==2.12.0
tensorflow-io-gcs-filesystem==0.32.0 <br>
termcolor==2.3.0
typing_extensions==4.5.0
tzdata==2023.3
urllib3==1.26.15
Werkzeug==2.3.3 <br>


## commits:

El avance del proyecto se encuetra en las siguientes ramas:

main<br>
AdvanceFE -> Cesar e Isabella<br>
AdvanceBE -> Cesar y Gianpier<br>
  


## Funcionalidades de la app:
- Matchear
	La app debe ser capaz de matchear de forma "inteligente" a los usuarios, mostrandoles primero los que más podrían encajar con ellos

- Posts
	La app tiene un sistema de posts que le permite al usuario compartir fotos, videos, comentarios o su vida en general. De este modo puede interactuar de mejor forma con la gente interesada en este.

- Monetización
	El usuario puede pagar por una cuenta premium que le permita acceder a más funcionalidades, como por ejemplo, ver a los usuarios que le dieron like. Ver los usuarios que observan su perfil o tener likes ilimitados

	Es justo en este punto en el que recalcamos que los likes para una cuenta gratuita son limitados. Es decir, una cuenta gratuita podrá dar hasta 15 likes diarios.

- Tipos de planes
	- Gratuito
		Las cuentas gratuitas pueden dar de 10 a 20 likes diarios y tienen acceso a los posts de los usuarios que le dieron like. Sin embargo tienen anuncios presentes en la app.
	- Premium
		Los premium tieneen hasta 50 likes por día y a diferencia de los gratuitos estos no poseen anuncios.
	- Vip
		Los usuarios VIP pueden observar a los usuarios que le dieron like, tienen likes ilimitados y no poseen anuncios.
