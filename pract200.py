import numpy as np
array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.sum(array , axis = 0))
print(np.mean(array , axis = 1))