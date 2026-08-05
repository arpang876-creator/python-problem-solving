marks = {
    "Arpan": 95,
    "Rahul": 35,
    "Priya": 78,
    "Amit": 29,
    "Sneha": 92,
    "Riya": 65,
    "Karan": 55
}
a = 0
b = 0
c = 0
d = 0
f = 0

for key, value in marks.items():
    if value >= 90:
        a += 1
    elif value >= 80:
        b += 1
    elif value >= 60:
        c += 1
    elif value >= 40:
        d += 1
    else:
        f+=1


print("Grade A:", a)
print("Grade B:", b)
print("Grade C:", c)
print("Grade D:", d)
print("Fail:", f)
