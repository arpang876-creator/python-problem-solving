#print above average

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
marks = 0
count = 0
Average = ""
for key,value in students.items():
    marks += value["Marks"]
    count += 1
Average = marks/count
print("Avg of marks ",Average)

for key,value in students.items():
    if value["Marks"] > Average:
        print(students[key])



