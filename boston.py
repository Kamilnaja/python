import tensorflow as tf
from keras.datasets import boston_housing
from tensorflow import keras

(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
