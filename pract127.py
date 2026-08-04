
marks = {
    "Arpan": 85,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}

total = 0
for key,value in marks.items():
    total += value
Avg = total/len(marks)
print("Average",Avg)

for key,value in marks.items():
    if value > Avg:
     print(key,":",value)
