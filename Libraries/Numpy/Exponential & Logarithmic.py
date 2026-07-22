import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"exp : {np.exp(data)}")
print("-" * 30)
print(f"log : {np.log(data)}")
print("-" * 30)
print(f"log 10  : {np.log10(data)}")
print("-" * 30)