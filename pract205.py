import numpy as np
array = np.array([10, 15, 20, 25, 30, 35])

print(np.where(array % 2 == 0, "Even" ,"Odd"))