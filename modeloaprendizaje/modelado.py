import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('rinderma.csv', delimiter=',')

citaideal = ['Salir a Comer', 'Ir al cine', 'Aire libre', 'Viaje', 'Evento artístico']
for cita in citaideal:
    data['Cuál seria tu idea de cita ideal?']=data['Cuál seria tu idea de cita ideal?'].str.split().apply(lambda x: 1 if cita in x else 0)
    data['Cuál seria tu idea de cita ideal?']=data['Cuál seria tu idea de cita ideal?'].astype(int)

data['¿Cuál es tu edad?']= data['¿Cuál es tu edad?'].astype(int)
data['¿Cuánto mides? (cm)']= data['¿Cuánto mides? (cm)'].astype(int)
data['¿Cuál es tu sexo?']= data['Sexo'].map({'Masculino': 0, 'Femenino': 1})

listageneros=['Clásica', 'Rock', 'Pop', 'Reguetón', 'Electrónica', 'otro']
for genero in listageneros:
    data['Genero de musica preferido']=data['Genero de musica preferido'].str.split().apply(lambda x: 1 if genero in x else 0)
    data['Genero de musica preferido']=data['Genero de musica preferido'].astype(int)



listapeliculas=['Drama', 'Thriller / suspense/', 'Comedia', 'Acción', 'Aventuras', 'Otro']
for pelicula in listapeliculas:
    data['Género de pelicula preferido']=data['Género de pelicula preferido'].str.split().apply(lambda x: 1 if pelicula in x else 0)
    data['Género de pelicula preferido']=data['Género de pelicula preferido'].astype(int)


deportespreferidos= ['Fútbol', 'Basket', 'Tenis', 'Natación', 'Atletismo', 'Otro']
for deporte in deportespreferidos:
    data['Deportes preferidos']=data['Deportes preferidos'].str.split().apply(lambda x: 1 if deporte in x else 0)
    data['Deportes preferidos']=data['Deportes preferidos'].astype(int)

data['¿Vas al gimnasio?']=data['¿Vas al gimnasio?'].map({'No':0, 'Si':1})
data['¿Te gusta salir mucho?']=data['¿Te gusta salir mucho?'].astype(int)
data['¿Te gusta beber?']=data['¿Te gusta beber?'].map.as_type(int)

oficios= ['Estudias', 'Trabajas', 'Ambos', 'Ninguno']
for oficio in oficios:
    data['¿A qué te dedicas?']=data['¿A qué te dedicas?'].str.split().apply(lambda x: 1 if oficio in x else 0)
    data['¿A qué te dedicas?']=data['¿A qué te dedicas?'].astype(int)


horientaciones= ['Heterosexual', 'Bisexual', 'Gay', 'otra']
for horientacion in horientaciones:
    data['Orientación Sexual']=data['Orientación Sexual'].str.split().apply(lambda x: 1 if horientacion in x else 0)
    data['Orientación Sexual']=data['Orientación Sexual'].astype(int)


hola=data['Deportes preferidos']

