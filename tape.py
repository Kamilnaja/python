# import tensorflow as tf

# x = tf.Variable(0.)
# with tf.GradientTape() as tape:
#   y = 1.5 * x + 3
# # This line prints the value of the gradient grad_of_y_wrt_x, which is 2. This indicates that for every unit change in the value of x, the value of y changes by 2 units.
# grad_of_y_wrt_x = tape.gradient(y, x)

# print(grad_of_y_wrt_x)


import tensorflow as tf

# x = tf.Variable(tf.random.uniform((2, 2)))
# with tf.GradientTape() as tape:
#   y = 3 * x + 3
# grad_of_y_wrt_x = tape.gradient(y, x)

# print(grad_of_y_wrt_x)

W = tf.Variable(tf.random.uniform((2, 2)))
b = tf.Variable(tf.zeros((2,)))
x = tf.random.uniform((2, 2))

with tf.GradientTape(persistent=True) as tape:
  y = tf.matmul(x, W) + b
grad_of_y_wrt_W = tape.gradient(y, [W, b])

# print(grad_of_y_wrt_W[0])

input_var = tf.Variable(initial_value=3.)

with tf.GradientTape() as tape:
  result = tf.square(input_var)
gradient = tape.gradient(result, input_var)

print(gradient)