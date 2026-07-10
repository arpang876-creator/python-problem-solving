numbers = [10, 5, 30, 20, 15]

largest=numbers[0]

for i in numbers:
    if i > largest:
        largest=i
numbers.remove(largest)
secondlarge=numbers[0]
for i in numbers:
    if i > secondlarge:
        secondlarge=i
print(secondlarge)