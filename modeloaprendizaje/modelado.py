import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('rinderma.csv', delimiter=',')

# columna de cita ideal
# ----------------------------------------------------------------------
# creo columnas para cada opción
for option in ['Salir a Comer', 'Ir al cine', 'Aire libre', 'Viaje', 'Evento artístico']:
    data[option] = data['¿Cuál seria tu idea de cita ideal?'].str.contains(option).astype('int8')

data.drop('¿Cuál seria tu idea de cita ideal?', axis=1, inplace=True)




# columna edad, estatura, sexo
# ----------------------------------------------------------------------
data['¿Cuál es tu edad?']= data['¿Cuál es tu edad?'].astype(int)
data['¿Cuánto mides? (cm)']= data['¿Cuánto mides? (cm)'].astype(int)
data['¿Cuál es tu sexo?']= data['¿Cuál es tu sexo?'].map({'Masculino': 0, 'Femenino': 1})


# columna de musica
# ----------------------------------------------------------------------
# crear columna para cada opción
for option in ['Clásica', 'Rock', 'Pop', 'Reguetón', 'Electrónica', 'otro']:
    data[option] = data['Género de musica preferido '].str.contains(option).astype('int8')

data.drop('Género de musica preferido ', axis=1, inplace=True)



# columna de peliculas
# ----------------------------------------------------------------------
for option in ['Drama', 'Thriller / suspense/', 'Comedia', 'Acción', 'Aventuras', 'Otro']:
    data[option] = data['Género de pelicula preferido'].str.contains(option).astype('int8')

data.drop('Género de pelicula preferido', axis=1, inplace=True)


# columna de deportes
# ----------------------------------------------------------------------
for option in ['Fútbol', 'Basket', 'Tenis', 'Natación', 'Atletismo', 'Otro']:
    data[option] = data['Deportes preferidos '].str.contains(option).astype('int8')

data.drop('Deportes preferidos ', axis=1, inplace=True)


# columna gimnasio, salir, beber
# ----------------------------------------------------------------------
data['¿Vas al gimnasio? ']=data['¿Vas al gimnasio? '].map({'No':0, 'Si':1})
data['¿Te gusta salir mucho?']=data['¿Te gusta salir mucho?'].astype(int)
data['¿Te gusta beber?']=data['¿Te gusta beber?'].astype(int)
data['¿A qué te dedicas?']=data['¿A qué te dedicas?'].map({'Estudias':0, 'Trabajas':1, 'Ambos':2, 'Ninguno':3}).astype(int)
data['Orientación Sexual']=data['Orientación Sexual'].map({'Heterosexual':0, 'Bisexual':1, 'Gay':2, 'otra':3}).astype(int)


#imprimir el dato 11
print(data.iloc[11])

#imprimir las columnas
print(data.columns)