marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}

student_name = input("Enter the name of the student:")
if student_name in marks:
    newmarks = input("Enter the new marks:")
    marks[student_name] = int(newmarks)
else:
    print("Student not found")


print(marks)