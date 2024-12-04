# adding element of list with other list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []
for x, y in zip(list1, list2):
    result.append(x + y)
print(result)

# adding element of array with other array
import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([10, 20, 30])
result = array1 + array2
print(result)


import time

list1 = range(1000000)
list2 = range(1000000)

start = time.time()
result = [x + y for x, y in zip(list1, list2)]
end = time.time()
print("List addition time taken :", end - start)


import numpy as np

arr1 = np.arange(1000000)
arr2 = np.arange(1000000)
start = time.time()
arr3 = arr1 + arr2
end = time.time()
print("Time taken for array :", end - start)

# array is much more faster than list
