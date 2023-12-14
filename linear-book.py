import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Define the number of samples per class
num_samples_per_class = 1000

# Generate negative samples from a multivariate normal distribution
negative_samples = np.random.multivariate_normal(mean=[0, 3], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

# Generate positive samples from a multivariate normal distribution
positive_samples = np.random.multivariate_normal(mean=[3, 0], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

# Combine the negative and positive samples into a single input matrix
inputs = np.vstack((negative_samples, positive_samples)).astype(np.float32)

# Create target vectors for each sample (0 for negative, 1 for positive)
targets = np.vstack((np.zeros((num_samples_per_class, 1), dtype="float32"), np.ones((num_samples_per_class, 1), dtype="float32")))

# Plot the input data points
plt.scatter(inputs[:, 0], inputs[:, 1], c=targets[:, 0])
plt.show()

# Define the dimensions of the input and output layers
input_dim = 2
output_dim = 1

# Initialize the weights matrix using random uniform values
W = tf.Variable(initial_value=tf.random.uniform(shape=(input_dim, output_dim)))

# Initialize the bias vector as zeros
b = tf.Variable(initial_value=tf.zeros(shape=(output_dim,)))

# Define the model function
def model(inputs):
    # Perform matrix multiplication between inputs and weights, and add the bias
    return tf.matmul(inputs, W) + b

# Define the square loss function
def square_loss(targets, predictions):
    # Calculate the squared difference between targets and predictions
    per_sample_losses = tf.square(targets - predictions)

    # Compute the average loss over all samples
    return tf.reduce_mean(per_sample_losses)

# Set the learning rate for optimization
learning_rate = 0.1

# Define the training step function
def training_step(inputs, targets):
    # Create a GradientTape to track gradients
    with tf.GradientTape() as tape:
        # Calculate the model predictions
        predictions = model(inputs)

        # Compute the loss using the square loss function
        loss = square_loss(targets, predictions)

    # Calculate the gradients of the loss with respect to the weights and bias
    grad_loss_wrt_W, grad_loss_wrt_b = tape.gradient(loss, [W, b])

    # Update the weights using the gradients and learning rate
    W.assign_sub(grad_loss_wrt_W * learning_rate)
    b.assign_sub(grad_loss_wrt_b * learning_rate)

    # Return the loss value
    return loss

# Train the model for 20 steps
for step in range(20):
    # Perform a training step using the inputs and targets
    loss = training_step(inputs, targets)

    # Print the loss value at each step
    print(f"Loss at step {step}: {loss:.4f}")

# Generate predictions for all input points
predictions = model(inputs)

# Plot the input data points and color them based on the predictions (darker for positive)
plt.scatter(inputs[:, 0], inputs[:, 1], c=predictions[:, 0] > 0.5)

# Generate x-values for plotting the decision boundary
x = np.linspace(-1, 4, 100)

# Calculate the corresponding y-values for the decision boundary
y = - W[0] / W[1] * x + (0.5 - b) / W[1]

# Plot the decision boundary as a red line
plt.plot(x, y, "-r")

# Plot the input data points again
plt.scatter(inputs[:, 0], inputs[:, 1], c=predictions[:, 0] > 0.5)
plt.show()