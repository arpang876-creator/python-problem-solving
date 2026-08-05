import csv
with open("students.csv","r") as f:
    data = csv.DictReader(f)
    for row in data:
        print(row)