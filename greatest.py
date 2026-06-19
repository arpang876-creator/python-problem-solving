#largest or greatest of 4 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))
if(a>=b and a>=c and a>=d):
    print("a is largest")
elif(b>=c and b>=d):
    print("b is largest")
elif(c>=d):
    print("c is largest")
else:
    print("d is largest")
