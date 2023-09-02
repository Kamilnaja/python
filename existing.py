import numpy as np

x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)

tup = (1, 2, 3)
b = np.asarray(tup)
print(b)

s = 'Hello World'
c = np.frombuffer(s, dtype='S1')
