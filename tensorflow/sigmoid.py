import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-10, 10, 100)
y = sigmoid(x)

plt.plot(x, y)
plt.show()
