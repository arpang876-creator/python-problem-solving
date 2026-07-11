numbers = [10, 25, 8, 40, 15]
largest= numbers[0]
def largest_num(numbers):
    largest= numbers[0]
    for i in numbers:
        if i > largest:
         largest = i
    return largest
        

highest = largest_num(numbers)
print(highest)