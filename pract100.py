#file handling

#1
with open("notes.txt","w") as file:
    file.write("name:Arpan")
    file.write("\nage:20")
    file.write("\ncity:mumbai")
    
#2
with open("fruit.txt","w") as file:
    file.write("apple")
    file.write("\nmango")
    file.write("\nbanana")
#3
with open("notes.txt","a") as file: #append
    file.write("C++")

#4
with open("student.txt","r") as file:
    file.read()

#5
with open("marks.txt","r") as file:
    for i in file:
      print(i)

#6
with open("subject.txt","r") as file:
    total=0
    for i in file:
        total+=1
    print("Total number of lines:",total)
        

