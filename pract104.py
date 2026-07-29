with open("student.txt","r") as f:
    data = f.readlines()
    
    sum=0
    for i in data:
        sum+=int(i)
    print(sum)
    print(len(data))


        