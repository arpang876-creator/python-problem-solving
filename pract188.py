import numpy as np

arr = np.array([5, 12, 7, 20, 3, 15, 8])

total = 0
for i in arr:
    total += i
avg = total / len(arr)
print(avg)


#numpy made in functions

print(np.mean(arr))