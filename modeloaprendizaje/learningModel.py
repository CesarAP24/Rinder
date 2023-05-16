import tensorflow
from tensorflow import keras
from modelado import data

##modelar un autoencoder de 33 datos de entrada y 256 datos de salida


#encoder from 34 to 64 output
from keras.layers import Input, Dense
from keras.models import Model
from keras import regularizers

capa_Incrementadora = keras.Sequential([
keras.layers.Dense(46, activation='leaky_relu', input_shape=[30]),
keras.layers.Dense(100, activation='leaky_relu'),
keras.layers.Dense(100, activation='leaky_relu')
])

capa_Decrementadora = keras.Sequential([
keras.layers.Dense(100, activation='leaky_relu', input_shape=[100]),
keras.layers.Dense(46, activation='leaky_relu'),
keras.layers.Dense(30, activation='leaky_relu')
])


autoencoder = keras.Sequential([capa_Incrementadora, capa_Decrementadora])


#complar

autoencoder.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
capa_Incrementadora.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
capa_Decrementadora.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
#define the test data
test_data = data[0:25]
test_data = test_data.astype('float32')

#define the training data
training_data = data[25:]
training_data = training_data.astype('float32')

autoencoder.fit(training_data, training_data, epochs=700, batch_size=15, shuffle=True)



#test and show
encoded_imgs = autoencoder.predict(test_data)
#print first case
print(encoded_imgs)
print(test_data)


#save the model
autoencoder.save('matches.h5')
 

#save incrementadora and decrementadora
capa_Incrementadora.save('capa_Incrementadora.h5')
capa_Decrementadora.save('capa_Decrementadora.h5')