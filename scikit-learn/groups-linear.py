import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model

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

X_train, X_test, y_train, y_test = train_test_split(inputs, targets, test_size=0.2)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test.reshape(-1, 1))

print("Coefficients: \n", model.coef_)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))


# Plot outputs
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="red", linewidth=1)
plt.yticks(())

plt.show()