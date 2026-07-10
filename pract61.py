#Write a function that takes three numbers and returns the largest.


def num(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
    

a=int(input("Enter any number"))
b=int(input("Enter any number"))
c=int(input("Enter any number"))

largest = num(a,b,c)
print( "largest number is",largest)