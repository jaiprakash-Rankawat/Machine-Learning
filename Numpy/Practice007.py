# matrix operation

# 1. dot operator

import numpy as np

arr1 = np.array([10, 20])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Dot Operator :", np.dot(arr1, arr2))


# 2. Transpose of a matrix

arr1 = np.array([[1, 2], [3, 4]])
print("Transpose :", np.transpose(arr1))


# For finding inverse and determenant we have to use "numpy.linalg"
from numpy.linalg import det, inv

print("Determenant :", det(arr1))
print("Inverse :", inv(arr1))
