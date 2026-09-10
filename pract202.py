import numpy as np
array = np.array([10, 25, 40, 15, 60])

print(np.where(array > 30,array + 100,array))
