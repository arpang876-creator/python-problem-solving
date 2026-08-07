import csv
with open("class.csv","r") as f:
    data = csv.DictReader(f)
    Avg = ""
    marks = 0
    length = 0

    for row in data:
        marks += int(row["Marks"])
        length +=1
    Avg = marks/length

with open("class.csv","r") as f:
    data = csv.DictReader(f)
    for row in data:
        if int(row["Marks"]) > Avg:
           print(row["Name"], ":", row["Marks"])
