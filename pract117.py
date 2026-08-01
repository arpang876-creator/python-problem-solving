with open("story.txt","r") as f:
    data = f.read().split()
    count = 0
    for i in data:
        if len(i) > 5:
            count += 1

    print(count)
