import csv
with open("students.csv","r") as f:
    data = csv.DictReader(f)

    name = input("Enter the name of the student: ")

    for row in data:
        if row["Name"] == name:
            print(name,":",row["Age"],":",row["Marks"])
        
    else:
        print("Student not found")
