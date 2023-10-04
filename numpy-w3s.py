import numpy as np

arr1 = np.array(42)
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr5 = np.array([1, 2, 3, 4], ndmin=5)
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr = np.array([1, 2, 3, 4, 5, 6, 7])

x = arr.copy()
arr[0] = 42

arr = np.array([1.1, 2.2, 3.3, 4.5, 5.1])
newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
