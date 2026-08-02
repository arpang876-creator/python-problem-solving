#pass or fail

marks = {
    "Arpan": 85,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92
}
Pass = 0
Fail = 0
for key,value in marks.items():
    if value >= 40:
        print(key,value,"PASS")
        Pass += 1
    else:
        print(key,value,"FAIL")
        Fail += 1

print("PASS",Pass)
print("FAIL",Fail)