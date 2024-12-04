# File input and output

import numpy as np

# saving array to Array.txt file
arr = np.array([10, 20, 30, 40, 50, 60])
np.savetxt("Array.txt", arr, delimiter=",", fmt="%d")
print("Saving Array.txt !")


# loading data from "Array.txt"
loaded_arr = np.loadtxt("Array.txt", delimiter=",")
print(loaded_arr)


# saving array to binary file

np.save("arr.npy", arr)
print("Saving binary file :")

# loading array from binary file
load_arr = np.load("arr.npy")
print(load_arr)

# Numpy is completed !
