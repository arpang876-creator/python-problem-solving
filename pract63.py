def vowel(word):  
   count=0
   for i in word:        
        if i in 'aeiou':
         count+=1
   return count
        
    
word = input("Enter any word")
word = word.lower()

Total = vowel(word)
print(Total)

