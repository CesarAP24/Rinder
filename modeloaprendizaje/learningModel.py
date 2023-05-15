import tensorflow
import keras
from modelado import data

##modelar un autoencoder de 33 datos de entrada y 256 datos de salida


#encoder from 34 to 64 output
from keras.layers import Input, Dense
from keras.models import Model
from keras import regularizers

capa_Incrementadora = keras.sequential([
keras.layers.Dense(64, activation='relu', input_shape=[33]),
keras.layers.Dense(128, activation='relu'),
keras.layers.Dense(256, activation='relu')
])

capa_Decrementadora = keras.sequential([
keras.layers.Dense(128, activation='relu', input_shape=[256]),
keras.layers.Dense(64, activation='relu'),
keras.layers.Dense(33, activation='relu')
])