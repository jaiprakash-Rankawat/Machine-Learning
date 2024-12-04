# axis concept

import numpy as np

arr = np.array([[10, 20, 30], [1, 2, 3]])
print("Sum :", np.sum(arr))
print("Sum-axis1:", np.sum(arr, axis=1))
print("Sum-axis0:", np.sum(arr, axis=0))


# cumulative sum and product

print("cumulative sum :", np.cumsum(arr))
print("cumulative sum :", np.cumsum(arr, axis=1))
print("cumulative Product :", np.cumprod(arr))
print("cumulative Product :", np.cumprod(arr, axis=1))
