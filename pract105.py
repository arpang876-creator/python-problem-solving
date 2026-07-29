with open("numbers.txt", "r") as f:
    data = f.readlines()

largest = int(data[0])

for i in data:
    i = int(i)

    if i > largest:
        largest = i

print(largest)