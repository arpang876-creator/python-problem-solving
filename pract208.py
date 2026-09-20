import numpy as np

arraya = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arrayb = np.array([10,20,30])

print(arraya.flatten()) # Flatten the array to 1D

print(np.concatenate((arraya.flatten(), arrayb)))