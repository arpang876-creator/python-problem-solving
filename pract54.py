numbers = [2, 4, 6, 8, 10]
initial=numbers[0]
largest=numbers[len(numbers)-1]
for i in numbers:
    if initial < i and largest > initial:
        initial = i
        continue
    print("sorted")
else:
    print("not sorted")





        
