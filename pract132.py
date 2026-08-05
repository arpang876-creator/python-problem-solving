marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}

for key,value in marks.items():
    if value > 80:
        print(key,":",value,"Grade:A")
    elif value > 60:
        print(key,":",value,"Grade:B")
    elif value > 40:
        print(key,":",value,"Grade:C")
    else:
        print(key,":",value,"Grade:F")
