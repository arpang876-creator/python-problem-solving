import csv

with open("record.csv","r") as f:
    info = csv.DictReader(f)

    highest = 0
    second_high=0
    name = ""
    high_name=""

    for i in info:
        if int(i["Marks"]) > highest:
            second_high = highest
            name = high_name
            highest = int(i["Marks"])
            high_name = i["Name"]

        elif int(i["Marks"]) > second_high:
            second_high = int(i["Marks"])
            name = i["Name"]
      
    print(high_name,":",highest)
    print(name,":",second_high)

            


