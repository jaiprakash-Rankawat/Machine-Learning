# Array operation

import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print(f"Addition :{arr1+arr2}")
print(f"Subtraction :{arr1-arr2}")
print(f"multiplication :{arr1*arr2}")
print(f"divide :{arr1/arr2}")
print(f"power :{arr1**arr2}")

# Bordcasting

# adding number to every element
arr = np.array([10, 20, 30])
print("Adding 10 :", arr + 10)


arr1 = np.array([[10, 20, 30], [40, 50, 60]])
arr2 = np.array([1, 2, 3])
arr3 = arr1 + arr2
print(arr3)


# Aggergate function

arr = np.array([10, 20, 30, 40, 50])
print("Minimum :", arr.min())
print("Maximum :", arr.max())
print("sum :", arr.sum())
print("Mean :", arr.mean())
print("Standard Deviation :", arr.std())

# min and max index
print("min Index :", arr.argmax())
print("max Index :", arr.argmin())
