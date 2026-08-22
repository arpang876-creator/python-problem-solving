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

for key,value in students.items():
    if int(value["Marks"]) > 80:
        print(key,value["Name"],value["Marks"])
