'''with open("story.txt","r") as f:
    data = f.read().split()
    print(len(data))'''


    
with open("story.txt","r") as f:
    data = f.read().split()
    print(data)

    largest = len(data[0])
    for i in data:
        word = i
        if len(i) > largest:
            largest = len(i)
    print(largest)
    
    
