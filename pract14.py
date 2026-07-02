m=int(input("Enter your marks"))

if m>=80:
    print("Grade A")
elif m>=70 or m<80:
    print("Grade B")
elif m>=60 or m<70:
    print("Grade C")
elif m>=45 or m<60:
    print("Grade D")
else:
    print("Grade F")
    