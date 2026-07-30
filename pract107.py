with open("subject.txt","r") as f:
    data =f.readlines()

    for lines in data:
        print(lines)
        print(len(lines))       
        print(len(lines.split()))