import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"cumsum: {np.cumsum(data)}") #حاصل جمع تجمیعی
print(f"cumprod: {np.cumprod(data)}") # حاصل ضرب تجمیعی