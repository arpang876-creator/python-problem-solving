

def small(*numbers):
    smallest = numbers[0]

    for i in numbers:
        if i < numbers[0]:
            smallest = i

    return smallest

print(small(8,9,7,6,5,4,3,3,2,1,0))
    