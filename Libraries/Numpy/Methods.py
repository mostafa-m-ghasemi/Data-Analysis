import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

data = np.array(data)
print(f'size of data: {data.size}')
print(f"items type: {data.dtype}")
print(f"Dim : {data.ndim}")
print(f"volume in RAM: {data.nbytes} bytes, and volume im memory {data.itemsize} bytes")
print(f"shape of data: {data.shape}")