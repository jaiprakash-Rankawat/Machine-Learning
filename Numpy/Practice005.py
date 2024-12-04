# Indexing and slicing

import numpy as np

# 1-D array
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[-1])
print(arr[:3])
print(arr[3:])
print(arr[1:5])
print(arr[::2])

# 2-D array

arr2D = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2D)
print(arr2D[1])
print(arr2D[1][0])
print(arr2D[1][1:])
print(arr2D[:2, :1])
