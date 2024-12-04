# np Range
import numpy as np

np_range = np.arange(1, 11)
print(np_range)
print(type(np_range))  # np_range is an array

# Linspace array = start , end , divide into specific parts

array1 = np.linspace(2, 10, 3)
print(array1)


# random

np_random = np.random.rand(2, 3)
# print values between 0 and 1 with 2 rows and 3 columns
print(np_random)

np_random = np.random.randint(1, 10, (2, 3))
# array with 2 rows and 3 colums but values within 1 to 10
print(np)
