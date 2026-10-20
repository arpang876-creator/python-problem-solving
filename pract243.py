str = input("Enter a word")

char={}

for i in str:
    if i in char:
        char[i] +=1
    else:
        char[i] = 1

print(char)
