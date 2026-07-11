numbers = [45, 12, 67, 3, 89]

def num(numbers):
    largest=numbers[0]
    smallest=numbers[0] 
    for i in numbers:
        if i > largest:
            largest = i
           
        if i < smallest:
            smallest = i

    print(f"largest",largest)
    print(f"smallest",smallest)

num(numbers)
