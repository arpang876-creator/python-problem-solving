marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}
topper = 0
lower = 100
name = ""
lowname = ""


for key,value in marks.items():
    if value > topper:
        topper = value
        name = key
    
    elif value < lower:
        lower = value
        lowname = key
print("Topper:", name, ":", topper)
print("Lowest:", lowname, ":", lower)
