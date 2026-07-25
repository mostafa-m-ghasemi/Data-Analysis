import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)

print(f"percential : {np.percentile(data, [25, 50, 75])}")
print("-" * 30)
print(f"quantile : {np.quantile(data, [0.25, 0.5, 0.75])}")
print("-" * 30)
print(f"corrcoef : {np.corrcoef(data[0, :], data[1, :])}")
print("-" * 30)
print(f"covariance : {np.cov(data[0, :], data[1, :])}")