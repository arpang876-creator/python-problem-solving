word = 'programming'
keys={}
for char in word:
    if char in keys:
        keys[char]+=1
    else:
        keys[char]=1

for i,j in keys.items():
    print(i,j)
