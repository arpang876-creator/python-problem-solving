marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}

name = input("Enter the name of the student")

if name in marks:
    print(name, ":", marks[name])

else:
    print("Student not found")