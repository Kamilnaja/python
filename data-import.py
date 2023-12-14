import numpy as np
import pandas as pd

# Define the number of samples per class
num_samples_per_class = 1000

# Generate negative samples
mean = [0, 3]
cov = [[1, 0.5], [0.5, 1]]
negative_samples = np.random.multivariate_normal(
    mean, cov, size=num_samples_per_class)

# Generate positive samples
mean = [0, 3]
cov = [[1, 0.5], [0.5, 1]]
positive_samples = np.random.multivariate_normal(
    mean, cov, size=num_samples_per_class)

# Combine samples into a single array
samples = np.vstack((negative_samples, positive_samples))

# Create labels array
labels = np.concatenate(
    (np.zeros(num_samples_per_class), np.ones(num_samples_per_class)))

# Create a DataFrame
data = pd.DataFrame(
    {'x1': samples[:, 0], 'x2': samples[:, 1], 'label': labels})

# Save the DataFrame to a Google Spreadsheet
data.to_csv('data.csv', index=False)
