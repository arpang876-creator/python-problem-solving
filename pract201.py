import numpy as np

array = np.array([10, 25, 40, 55, 70, 85])

print(array[(array > 30) & (array < 80)])

print(array[(array >= 20) & (array <= 60)])