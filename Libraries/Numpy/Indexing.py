import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"max : {np.max(data)} and max number index : {np.argmax(data)}")
print(f"min : {np.min(data)} and min number index : {np.argmin(data)}")