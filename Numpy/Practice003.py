# Attributes of array

# 1. size = total element
# 2. Dimensions = 1-D, 2-D
# 3. shape = (rows,columns)
# 4. dataType = int,float,etc.
# 5. itemsize =

import numpy as np

arr = np.array([[10, 20, 3000], [40, 50, 60]])
print(arr.size)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.itemsize)


# 3-D Array
arr_3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3D)
print(arr_3D.ndim)
print(arr_3D.shape)
print(arr_3D.size)
print(arr_3D.dtype)
print(arr_3D.itemsize)
