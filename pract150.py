try:
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    if b == 0:
        print("Denominator cannot be zero")
    else:
        c = a / b
        print("Division of b from a is:", c)
except ValueError:
    print("Invalid input")


