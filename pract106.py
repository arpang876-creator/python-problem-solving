with open("numbers.txt", "r") as f:
    data = f.readlines()
smallest = int(data[0])

for i in data:
    i = int(i)
    if i < smallest:
        smallest = i
print(smallest)

