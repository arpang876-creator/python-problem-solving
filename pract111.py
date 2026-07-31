with open("source.txt","r") as f:
    data = f.read()
    print(data)

with open("destination.txt","w") as f:
    f.write(data)



