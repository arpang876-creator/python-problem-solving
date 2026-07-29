with open("student.txt","w") as f:
    f.write("name:Arpan")
    f.write("\nage:20")
    f.write("\ncity:Mumbai")

with open("student.txt","r") as f:
     data = f.readlines()
     f.seek(0)
     count = f. read()
     print(len(data))
     print(len(count))

    
    

  
     
