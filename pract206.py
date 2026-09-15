import numpy as np
array = np.array([10, 15, 20, 25, 30])

print(np.where( array > 20, array *2 ,array + 5))