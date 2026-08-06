import csv
with open("students.csv", "r") as f:
    data = csv.DictReader(f)

    student_name = input("Enter the name of the student: ")
    for row in data:
        if student_name in row["Name"]:
            del row["Name"]
            print("Deleted successfully")
        else:
            print("Student not found")

        

rows = []

for row in data:
    if row["Name"] != student_name:
        rows.append(row)
