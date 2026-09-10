import numpy as np
array = np.array([5, 15, 25, 35, 45])

print(np.where(array < 20, 0, array))