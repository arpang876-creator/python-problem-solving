with open("story.txt","r") as f:
    data = f.read().split()

    lowest = data[0]
    for i in data:
        if len(i) < len(lowest):
            lowest = i
    print(lowest)