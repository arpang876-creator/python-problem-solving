import csv

with open("record.csv", "r") as f:
    data = csv.DictReader(f)

    youngest = 100
    name = ""

    for row in data:
        if int(row["Age"]) < youngest:
            youngest = int(row["Age"])
            name = row["Name"]

print("Youngest student is:", name, ":", youngest)