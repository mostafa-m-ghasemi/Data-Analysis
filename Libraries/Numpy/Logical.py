import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f" all: {np.all(data > 5)}")
print(f" any: {np.any(data > 5)}")