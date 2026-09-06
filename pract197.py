import numpy as np

array = np.array([10, 25, 5, 40, 15, 30])

array[array > 20] += 5
print(array)

array[array > 25] *= 2
print(array)