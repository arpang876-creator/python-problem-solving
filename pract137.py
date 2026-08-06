import csv
with open("students.csv","r") as f:
    data = csv.DictReader(f)

    for row in data:
       marks = int(row["Marks"])
       if marks > 80:
        print(row["Name"], ":", marks)
