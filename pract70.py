#Write a function that calculates the area of a rectangle.If the width is not provided, assume it is 10.

def area(length,breadth=10):
    a = length * breadth
    return a


A_rectangle=area(5)
print(A_rectangle)
