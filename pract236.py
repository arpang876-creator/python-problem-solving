
n = input("Enter a number:")

vow = 0

for i in n:
    if i in "aeiouAEIOU":
        vow += 1
print("Number of vowels:",  vow)