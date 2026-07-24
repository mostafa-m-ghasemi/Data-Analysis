import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"round : {np.round(data)}")
print("-" * 30)
print(f"floor : {np.floor(data)}")
print("-" * 30)
print(f"ceiling : {np.ceil(data)}")
print("-" * 30)
print(f"truncate : {np.trunc(data)}")
print("-" * 30)