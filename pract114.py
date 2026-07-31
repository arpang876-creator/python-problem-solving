with open("sample.txt","r") as f:
    data = f.read()

    
    vowel = 0
    consonant = 0
    for i in data:
        if i in "aeiou" or i in "AEIOU":
            vowel += 1
        elif ("a" <= i <= "z") or ("A" <= i <= "Z"):
            consonant += 1
 
    print("Vowels", vowel)
    print("Consonants",consonant)
