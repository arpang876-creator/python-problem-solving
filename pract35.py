#counting vowels in a string
string=input("Enter any string")
vow=0
cons=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vow+=1
    else:
        cons+=1
print("There are %s vowels in the string"%vow)
print("There are %s consonants in the string"%cons)
