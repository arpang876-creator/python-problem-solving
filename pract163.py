#Find the Average Marks

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
len = 0
Average = ""
for key,value in students.items():
    marks += value["Marks"]
    len += 1
Average = marks/len
print("Avg of marks ",Average)
