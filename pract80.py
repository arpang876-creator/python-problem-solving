
def large(*numbers):
    numbers=list(numbers)
    largest=numbers[0]

    for i in numbers:
        if i > largest:
            largest = i
    return largest

def rem_largest(*numbers):
    numbers = list(numbers)
    largest = large(*numbers)

    numbers.remove(largest)
    return numbers

def sec_largest(*numbers):
    numbers = rem_largest(*numbers)
    second_largest=numbers[0]
     
    for j in numbers:
        if j > second_largest:
           second_largest=j
    return second_largest
     


print(sec_largest(1,2,5,7,9,11,12,17,13,14))





        
    


            