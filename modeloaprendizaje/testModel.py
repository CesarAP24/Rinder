import tensorflow
from tensorflow import keras
from modelado import data

data = data.astype('float32')

#importar el modelo de .h5
matches = keras.models.load_model('matches.h5')
incrementador = keras.models.load_model('capa_Incrementadora.h5')
decrementador = keras.models.load_model('capa_Decrementadora.h5')

#testear un caso random del data
test_data = data[0:2]
test_data = test_data.astype('float32')

increment_results = incrementador.predict(test_data)
decrement_results = decrementador.predict(increment_results)

#printear resultados
print("Test data:")
print(test_data)
print()
print("Increment results:")
print(increment_results)
print()
print("Final results:")
print(matches.predict(test_data))

keras.utils.plot_model(matches, to_file='model.png')