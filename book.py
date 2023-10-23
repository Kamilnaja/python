import numpy as np
from matplotlib import pyplot as plt

# from Chollet book
num_samples_per_class = 1000

negative_samples = np.random.multivariate_normal(
    mean=[0, 3],
    cov=[[1, 0.5], [0.5, 1]],
    size=num_samples_per_class
)

positive_samples = np.random.multivariate_normal(
    mean=[3, 0],
    cov=[[1, 0.5], [0.5, 1]],
    size=num_samples_per_class
)


plt.scatter(negative_samples.flatten(),
            positive_samples.flatten(), alpha=0.5, c='red')
plt.draw()
plt.show()
