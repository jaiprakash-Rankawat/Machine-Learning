# importing numpy
import numpy as np

# creating 1-D array
arr1D = np.array([10, 20, 30])
print(arr1D)

# creating 2-D array
arr2D = np.array([[10, 20, 30], [40, 50, 60]])  # 2 Row, 3 columns
print(arr2D)

# accessing element of 2nd row and 1st column
print(arr2D[1][0])


# specifying data types
arr = np.array([1, 2, 3], dtype="float")  # array with float data type
print(arr)


# matrix with zeros
matrix = np.zeros((2, 3))  # 2 rows and 3 columns
print(matrix)


# matrix with ones
matrix = np.ones((2, 3))
print(matrix)

# identity matrix
matrix = np.eye(4)
print(matrix)
