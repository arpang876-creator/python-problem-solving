#prime number or not

n=int(input("Enter any number"))
if n <= 1:
    print("it is not a prime number")

for i in range(2,n):
    if(n%i==0):
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
