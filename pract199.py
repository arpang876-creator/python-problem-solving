import numpy as np
array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(array[1,:] + 10) 

array[2,:] += 100
print(array)

array[:,1] *= 3

print(array)