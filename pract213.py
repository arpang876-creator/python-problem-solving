import numpy as np
array = np.array([10, 25, 40, 15, 60, 35, 5])

'''
count = 0 
for x in array:
    if x > 20:
        count+=1

print(count)'''


print(np.sum(array > 20))