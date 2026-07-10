list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3=[]

for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
            break

print(list3)