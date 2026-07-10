numbers = [1, 2, 2, 3, 4, 2, 5]
'''total=0
for i in numbers:
    if i == 2:
        total+=1
print(total)'''


total=[i for i in numbers if i == 2]
print(len(total))