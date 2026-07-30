with open("article.txt","r") as f:
    word = input("Enter word")
    data = f.read().split()


    for i in data:
        if i == word:
            print("Word exist")
            break
    else:
        print("Word doesnt exist")
        