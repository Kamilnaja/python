import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train/255.0
x_test = x_test/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.2),  # czemu 0.2?
    keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()

predictions = tf.nn.softmax(predictions).numpy()

print(predictions)

# czemu from logits
loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)


model.compile(optimizer="adam",
              loss=loss_fn,
              metrics=["accuracy"])

model.fit(x_train, y_train, epochs=5)

probability_model = keras.Sequential([
    model,
    keras.layers.Softmax()
])

print(probability_model(x_test[:5]))
