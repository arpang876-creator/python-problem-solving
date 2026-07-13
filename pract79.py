#avg of numbers


def avg(*numbers):
    total = 0
    average=0
    for i in numbers:
        total+=i
        average = total / len(numbers)

    return average

print(avg(10,20,30,40))