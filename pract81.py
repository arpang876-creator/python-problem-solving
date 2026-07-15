#second largest

def sec_large(*numbers):
    largest = numbers[0]
    second = numbers[0]

    for i in numbers:
        if i > largest:    
         second=largest
         largest = i

        elif second > largest:
           largest=second

    return second


print(sec_large(1,2,3,4,5,6,7,8,9,10,11))


