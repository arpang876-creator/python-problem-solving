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
    print("The average marks is:", Avg)
