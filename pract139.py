import csv
with open("students.csv", "r") as f:
    data = csv.DictReader(f)
    student_name = input("Enter the name of the student: ")
    new_marks=int(input("Enter the new marks"))

    for row in data:
        if student_name in row["Name"]:
            row["Marks"] = new_marks
            print("Marks updated sucessfully")
            break
    else:
        print("Student not found") 

        Data = list(data) 
        with open("students.csv", "w", newline="") as f:
            fieldnames = ["Name", "Age", "Marks"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(Data)

    

