import csv
with open("record.csv","r") as f:
    info = csv.DictReader(f)

    passs = 0
    fail=0

    for i in info:
        if int(i["Marks"]) >= 40:
            passs += 1
        else:
            fail +=1

    print("Total number of students passed",passs)
    print("Total number of students failed",fail)



