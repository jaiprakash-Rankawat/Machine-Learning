# Handling Missing data

import numpy as np

# 1. Representing missing data
arr = np.array([10, 20, np.nan, 40, 50])
print(arr)

# 2. identifying missing data
print(np.isnan(arr))

# 3. counting missing data
count = np.sum(np.isnan(arr))
print("Total Missing Value :", count)

# 4. removing missing data
new_arr = arr[~np.isnan(arr)]
print(new_arr)

# 5. Filling missing Value
mean_value = np.nanmean(arr)
new_arr = np.where(np.isnan(arr), mean_value, arr)
print(new_arr)

# 6. Aggregate missing value
# ignoring missing value
print("sum :", np.nansum(arr))
print("mean :", np.nanmean(arr))
print("median :", np.nanmedian(arr))
