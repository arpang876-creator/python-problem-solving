#palindrome or not

n=int(input("Enter any number"))
strn=str(n)#strn is a string variable that stores the string representation of the input number n. This
if strn==strn[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
