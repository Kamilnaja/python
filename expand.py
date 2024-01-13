import numpy as np

X = np.random.random((32, 10))
y = np.random.random((10))

y = np.expand_dims(y, axis=0)

Y = np.concatenate([y] * 32, axis=0)

