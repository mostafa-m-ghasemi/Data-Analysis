import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
data = np.array(data)
data2 = np.array(data2)

print(f"dot : {np.dot(data, data2)}")
print("-" * 30)
print(f"matmul : {np.matmul(data, data2)}")
print("-" * 30)
print(f"linalg  : {np.linalg.inv(data)}")
print(f"linalg: {np.linalg.norm(data)}")
print(f"linalg: {np.linalg.det(data)}")
print(f"linalg: {np.linalg.eig(data)}")
