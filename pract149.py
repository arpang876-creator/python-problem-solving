#Exception handling

try:
    a = int(input("Enter a number"))
    b=int(input("Enter another number"))
    c = (a + b)/2
    print("The value is:",c)
except:
    print("Invalid input")
