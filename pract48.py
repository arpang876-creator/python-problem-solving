numbers = [25, 18, 90, 12, 67]

lowest=numbers[0]

for i in numbers:
    if i < lowest:
        lowest=i
print(lowest)