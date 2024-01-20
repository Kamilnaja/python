import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


learing_rate = 0.01
training_epochs = 100

x_train = np.linspace(0, 10, 100)
y_train = x_train + np.random.normal(0,1,100);


weights = tf.Variable(0.)
bias = tf.Variable(0.)

def linreg(x):
  y = weights * x + bias
  return y

# MSE
def squared_error(y_pred, y_true):
  return tf.reduce_mean(tf.square(y_pred - y_true))

for epoch in range(training_epochs):
  with tf.GradientTape() as tape:
    y_pred = linreg(x_train)
    loss = squared_error(y_pred, y_train)

    gradients = tape.gradient(loss, [weights, bias])
    # Update ref by subtracting value from it.
    weights.assign_sub(learing_rate * gradients[0])
    bias.assign_sub(learing_rate * gradients[1])

    print(f"Epoch count {epoch}: Loss value: {loss.numpy()}")


plt.scatter(x_train, y_train)
plt.plot(x_train, linreg(x_train), 'r')
plt.show()