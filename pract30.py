n=int(input("Enter any number:"))
for rows in range(n,0,-1):
    for stars in range(rows):
        print(f"{stars + 1}",end="")
    print()