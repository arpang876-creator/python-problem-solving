#Write a function that returns the second largest number in a list.
numbers = [89]

def sec_largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:           
            largest = i
    return largest
        

        
large = sec_largest(numbers)
numbers.remove(large)

secondlarge = sec_largest(numbers)
print(secondlarge)