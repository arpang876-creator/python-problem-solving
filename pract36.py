#check whether the given string is palindrome or not
str=input("Enter any string")
rev=str[::-1]
if str==rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print (rev)