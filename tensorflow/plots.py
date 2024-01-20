import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

HOW_MANY = 3000

x = tf.ones(shape=(12, 1))
x = tf.zeros(shape=(2, 1))

y = tf.random.normal(shape=(HOW_MANY, 1), mean=0., stddev=1)

x = tf.random.uniform(shape=(HOW_MANY, 1), minval=0., maxval=1.)

normal = np.array(y.numpy()).flatten()

plt.hist(normal)
plt.title("Normal distribution")
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()

uniform = np.array(x.numpy()).flatten()

plt.hist(uniform)
plt.title("Normal distribution")
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()
