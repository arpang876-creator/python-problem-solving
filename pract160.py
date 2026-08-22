students = {
    "student1": {
        "Name": "Arpan",
        "Age": 20,
        "Marks": 95
    },
    "student2": {
        "Name": "Rahul",
        "Age": 21,
        "Marks": 78
    },

        "student3" : {
            "Name" : "Arnav",
            "Age" : 17,
            "Marks" : 93
    }
}

name = input("Enter a name ")
for key,value in students.items():
    if value["Name"] == name:
        print("Name",value["Name"])
        print("Age", value["Age"])
        print("Marks",value["Marks"])
        break
        
else:
    print("The name given doesnt exist")
        
