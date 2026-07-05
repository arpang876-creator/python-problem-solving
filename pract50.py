numbers = [10, 20, 30, 40, 50]
newlist = []

for i in range(len(numbers)-1,-1,-1):
    newlist.append(numbers[i])

print(newlist)