import numpy as np
import tensorflow as tf
from keras.datasets import imdb
from tensorflow import keras

(train_data, train_labels), (test_data,
                             test_labels) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()

reverse_word_index = dict([(value, key)
                          for (key, value) in word_index.items()])
decoded_review = ' '.join([reverse_word_index.get(i-3, '?')
                           for i in train_data[0]])


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            results[i, j] = 1.
    print('results', results)
    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
