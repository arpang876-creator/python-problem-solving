import csv
with open("record.csv","r") as f:
    data = csv.DictReader(f)

    total = 0
    passed = 0
    fail = 0

    for i in data:
        total += 1
        marks = int(i["Marks"])
        if marks > 40:
            passed +=1
            print(i["Name"],i["Marks"],"PASS")
        else:
            fail +=1
            print(i["Name"],i["Marks"],"FAIL")

    print("\nTotal students",total)
    print("Passed",passed)
    print("Failed",fail)
    print("Percentage passed",(passed/total)*100)