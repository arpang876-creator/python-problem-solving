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
    }
}

highest = 0
name = ""

for key,value in students.items():
    val = int(value["Marks"])
    if val > highest:
        highest = val
        name = value["Name"]
print(name)
print(highest)
