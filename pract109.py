with open("sample.txt","r") as f:
    data = f.read()

    Uppercase = 0 
    Lowercase = 0
    DigitCount = 0
    special = 0

    for i in data:
       Upper = i.isupper()
       Lower = i.islower()
       IsDigit = i.isdigit()

       if Upper is True:
           Uppercase += 1
       elif IsDigit is True:
           DigitCount += 1
       elif Lower is True:
           Lowercase += 1
       else:
           special += 1

    print("Uppercase:", Uppercase)
    print("Lowercase:", Lowercase)
    print("Digits:", DigitCount)
    print("Special:", special)


       
           
           
           

    


    

    