from keras import Input, layers
from tensorflow import keras as Keras

inputs = Input(shape=(3, 0), name='myInput')
features = layers.Dense(64, activation='relu')(inputs)
outputs = layers.Dense(10, activation='softmax')(features)
model = Keras.Model(inputs, outputs)
model.build(input_shape=(None, 3))
print(model.summary())
Keras.utils.plot_model(model, 'my_first_model.png')
