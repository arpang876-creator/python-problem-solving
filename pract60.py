'''Write a function that takes a number as a parameter and prints:

"Even" if the number is even
"Odd" if the number is odd'''


def num(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("odd")

n=int(input("Enter any number"))

num(n)