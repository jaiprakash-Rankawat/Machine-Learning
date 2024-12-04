# Logical opeator

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr > 30)
# output : [False False False  True  True]

# logical and operator
arr1 = np.array([1, 5, 2, 7, 3])
print(np.logical_and(arr < 30, arr1 > 4))
# output : [False  True False False False]


# sorting
print("Sorting :", np.sort(arr1))

# Searching
indices = np.where(arr > 30)
print("Searching :", indices)
