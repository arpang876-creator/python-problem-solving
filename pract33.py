n=int(input("Enter any number:"))
for rows in range(1, n + 1,2):
    for stars in range(rows):
        print(f"*",end="")
    print()