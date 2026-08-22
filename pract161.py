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

name = input("Enter  a name")
new_marks = int(input("Enter new marks"))

for key,value in students.items():
    if value["Name"] == name:
        value["Marks"] = new_marks
        print("Name",value["Name"])
        print("Marks",value["Marks"])
    