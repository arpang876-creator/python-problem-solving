import numpy as np
array = np.array([10, 20, 30, 40, 50])

array[array > 30] = 0

array[array < 15] = -1

print(array)