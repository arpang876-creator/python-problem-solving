#Find the second highest marks and print:
marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}

highest = 0
second_highest = 0
student_name = ""

for key,value in marks.items():
    if value > highest:
        highest = value
        for key,value in marks.items():
            if value > second_highest and value < highest:
                second_highest = value
                student_name = key

print("Second highest marks:",student_name,":",second_highest)    

    
    