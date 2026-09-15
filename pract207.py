import numpy as np
array = np.array([10, 25, 40, 55, 70, 85])

print(np.where((array >= 30) & (array <= 70),1,0))

print(np.where((array % 3 == 0), 1, 0))