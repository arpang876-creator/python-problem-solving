'''numbers = [25, 18, 90, 12, 67]

for i in numbers:
    if i >= 90:
        print("highest number is %d",i)
    else:
        pass
'''


numbers = [25, 111, 90, 12, 95]
largest=numbers[0]
for i in numbers:
    if i > largest:
        largest=i
print(largest)