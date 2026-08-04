#Calculate Average Marks

marks = {
    "Arpan": 85,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}
Total = 0
for key,value in marks.items():
    Total += value
print(Total)
Average = Total/len(marks)
print("Average Marks:",Average)