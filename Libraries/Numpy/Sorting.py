import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"sort : {np.sort(data)}")
print("-" * 30)
print(f"argsort : {np.argsort(data)}")