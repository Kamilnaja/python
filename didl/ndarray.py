from matplotlib import pyplot as plt
import tensorflow as tf
x = tf.range(12, dtype=tf.float32)
X = tf.reshape(x, (3, 4))

# print(tf.zeros((4, 2, 4)))
# print (tf.ones((4, 2, 4)))
# print (tf.random.normal(shape=[30, 4], stddev=0.01))

data = tf.random.normal(shape=[2, 200])

# print(data)

# plt.scatter(x=data[0], y=data[1], marker='x')
# plt.show()

# X_var = tf.Variable(X)
# print(X_var)
# X_var[1, 2].assign(9)
# print(X_var)
exp = tf.exp(x);
# print(exp)

x = tf.constant([1.0, 2, 4, 8])
y = tf.constant([2.0, 2, 2, 2])
# print(x + y, x - y, x * y, x / y, x ** y)

X = tf.reshape(tf.range(12, dtype=tf.float32), (3, 4))


Y = tf.constant([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
ct = tf.concat([X, Y], axis=0), tf.concat([X, Y], axis=1)
# print(ct)

# print(X == Y)
print(tf.reduce_sum(tf.reduce_sum(X)))