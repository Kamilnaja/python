import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from keras import layers
from tensorflow import keras

np.set_printoptions(precision=3, suppress=True)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["MPG", "Cylinders", "Displacement", "Horsepower", "Weight",
                "Acceleration", "Model Year", "Origin"]
raw_dataset = pd.read_csv(url, names=column_names,
                          na_values="?", comment="\t",
                          sep=" ", skipinitialspace=True)
dataset = raw_dataset.copy()

dataset = dataset.dropna()

dataset["Origin"] = dataset["Origin"].map({1: "USA", 2: "Europe", 3: "Japan"})

dataset = pd.get_dummies(dataset, prefix="", prefix_sep="")

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

sns.pairplot(
    train_dataset[['MPG', 'Cylinders', 'Displacement', 'Weight']], diag_kind='auto')
# plt.show()

train_dataset.describe().transpose()

train_features = train_dataset.astype(np.float32).copy()
test_features = test_dataset.astype(np.float32).copy()

train_labels = train_features.pop("MPG")
test_labels = test_features.pop("MPG")

train_dataset.describe().transpose()[["mean", "std"]]

normalizer = keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

print(normalizer.mean.numpy())

first = np.array(train_features[:1])
with np.printoptions(precision=2, suppress=True):
    print("First example:", first)
    print()
    print("Normalized:", normalizer(first).numpy())

horsepower = np.array(train_features["Horsepower"])
horsepower_normalizer = keras.layers.Normalization(
    input_shape=[1, ], axis=None)
horsepower_normalizer.adapt(horsepower)

horsepower_model = keras.Sequential([
    horsepower_normalizer,
    layers.Dense(units=1)
])

print(horsepower_model.summary())
predict = horsepower_model.predict(horsepower[:10])
print(predict)

horsepower_model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.1),
    loss="mean_absolute_error")

history = horsepower_model.fit(
    train_features["Horsepower"], train_labels,
    epochs=100,
    verbose=0,
    validation_split=0.2)

hist = pd.DataFrame(history.history)
hist["epoch"] = history.epoch
print(hist.tail())
