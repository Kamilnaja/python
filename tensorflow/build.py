import matplotlib.pyplot as plt
from keras import layers
from tensorflow import keras as Keras

model = Keras.Sequential([])
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.build(input_shape=(None, 3))
print(model.summary())

# plt.plot(model.weights[0][0], 'x')
# plt.show()
