import numpy as np

array = np.array([10, 25, 5, 40, 15, 30])

new_array = array[array > 20]
print(new_array * 2)