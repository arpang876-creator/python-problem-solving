#def largest numbers

def large(*numbers):
    largest=numbers[0]

    for i in numbers:
        if i > largest:
            largest=i
    print("largest number is",largest)
        

large(7,8,9,67,76,87,91,54,32)
    