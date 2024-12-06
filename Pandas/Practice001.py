# series and data-frame

import pandas as pd

# int dataType
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

# bool dataType
data = [False, True, False]
series = pd.Series(data)
print(series)

# Obj dataType (Mixed value)
data = [False, 1, 0, 1, 1]
series = pd.Series(data)
print(series)


# DataFrame
data = {"Name": ["Radha", "Krishna"], "Age": [30, 33]}
data_frame = pd.DataFrame(data)
print(data_frame)
