import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('obl2.csv')

data['amount'] = data['amount'].replace('(\,...zł)', '', regex=True)
data['amount'] = data['amount'].replace('\s+', '', regex=True)
data['amount'] = data['amount'].astype(int)
data['date'] = pd.to_datetime(data['date'])

x = data['amount'].values.reshape(-1, 1)
print(x)

model = LinearRegression()
model.fit(x, data[['amount']])
# inputs = data[['amount']]

# input_dim = 2
# output_dim = 1
# num_samples_per_class = 17

# W = tf.Variable(initial_value=tf.random.uniform(shape=(input_dim, output_dim)))
# b = tf.Variable(initial_value=tf.zeros(shape=(output_dim,)))

# targets = np.vstack((np.zeros((num_samples_per_class, 1), dtype="float32"),
#                      np.ones((num_samples_per_class, 1), dtype="float32")))


# def model(inputs):
#     return tf.matmul(inputs, W) + b


# def square_loss(targets, predictions):
#     per_sample_losses = tf.square(targets - predictions)
#     return tf.reduce_mean(per_sample_losses)


# learning_rate = 0.1


# def training_step(inputs, targets):
#     with tf.GradientTape() as tape:
#         predictions = model(inputs)
#         loss = square_loss(predictions, targets)
#     grad_loss_wrt_W, grad_loss_wrt_b = tape.gradient(loss, [W, b])
#     W.assign_sub(grad_loss_wrt_W * learning_rate)
#     b.assign_sub(grad_loss_wrt_b * learning_rate)
#     return loss


# for step in range(40):
#     loss = training_step(inputs, targets)
#     print(f"Loss at step {step}: {loss:.4f}")
