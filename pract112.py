with open("story.txt","r") as f:
    data = f.read().split()
    word = input("Enter the word")
    frequency = 0

    for i in data:
        if i == word:
            frequency +=1
    print(frequency)