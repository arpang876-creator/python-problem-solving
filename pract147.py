import csv
with open("record.csv","r") as f:
    data = csv.DictReader(f)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    for i in data:
        marks = int(i["Age"])
        if 20 >= marks >= 18:
            count_1 += 1 
        elif 22 >= marks > 20:
            count_2 +=1
        elif 24 >= marks > 22:
            count_3 += 1
        elif marks > 24:
            count_4 +=1

    print(count_1)
    print(count_2)
    print(count_3)
    print(count_4)

