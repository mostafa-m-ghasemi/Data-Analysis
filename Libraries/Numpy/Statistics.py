import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"mean : {np.mean(data)}")
print("-" * 30)
print(f"median : {np.median(data)}")
print("-" * 30)
print(f"std : {np.std(data)}")
print("-" * 30)
print(f"variance : {np.var(data)}")
print("-" * 30)
print(f"min : {np.min(data)}")
print("-" * 30)
print(f"max : {np.max(data)}")
print("-" * 30)
print(f"sum : {np.sum(data)}")
print("-" * 30)
print(f"product : {np.prod(data)}") # حاصلضرب