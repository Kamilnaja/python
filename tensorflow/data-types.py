import numpy as np
dt = np.dtype(np.int32)
print(dt)

import numpy as np 
dt = np.dtype('>i4') 
# print(dt)

a = np.array([[1, 2, 3, 0], [4, 5, 6, 6]])

b = np.array([[1,2,3],[4,5,6]]) 
b.shape = (1, 6)

d = np.arange(24)

b = d.reshape(2,4,3)
# print(b)

x = np.array([1,2,3,4,5], dtype=np.float32)
# print(x.itemsize)

# print(x.flags)

z = np.empty([3,2], dtype = int) 
print(z)

z1 = np.zeros(5, dtype = int)
print(z1)

z2 = np.ones(5, dtype = int)
print(z2)