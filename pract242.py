str = input("Enter a word")

for i in str:
    vow = 0
    if i=="a"or"e"or"i"or"o"or"u":
        vow += 1
    else:
        vow += 0

print("Total Vowel",vow)
    
