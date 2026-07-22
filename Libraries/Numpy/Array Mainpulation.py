import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"reshape : {data.reshape((3, 3))}")
print("-" * 30)
print(f" transpose : {np.transpose(data)}")
print("-" * 30)
print(f"concatenate : {np.concatenate(data)}")
print("-" * 30)
print(f"vstack : {np.vstack(data)}")
print("-" * 30)
print(f"hstack : {np.hstack(data)}")
