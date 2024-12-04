# Reshaping and Flattening

import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60])
# new_arr = arr.reshape(2, 3)
# print(arr)
# print(new_arr)


# flattening
# flat_arr = new_arr.flatten()
# print(flat_arr)

# Stacking and spliting

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical Stack
print("Vertical Stack:\n", np.vstack((arr1, arr2)))

# Horizontal Stack
print("Horizontal Stack:\n", np.hstack((arr1, arr2)))

# Spliting
split = np.array_split(arr1, 3)
print("Spliting :", split)
