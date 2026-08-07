import csv
highest = None
with open("class.csv", "r") as f:
    data = csv.DictReader(f)
    highest = 0

    for row in data:
        marks = int(row["Marks"])
        if marks > highest:
            highest = marks
    print("The highest marks is:", highest)
