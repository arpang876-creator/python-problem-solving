students = {
    "Arpan": 78,
    "Rahul": 35,
    "Aman": 56,
    "Priya": 28,
    "Neha": 90
}
count = 0
for keys,values in students.items():
    if values >= 40:
        count +=1
    else:
        count+=0
print("Student passed the exam",count)