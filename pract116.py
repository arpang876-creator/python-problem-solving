with open("story.txt","r") as f:
    letter = input("Enter any letter")
    data = f.read().split()

    words = 0

    for i in data:
        if i[0].lower() == letter.lower():
            words +=1
    print(words)
            