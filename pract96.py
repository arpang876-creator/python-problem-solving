marks = {
    "Math": 90,
    "English": 75,
    "Science": 98,
    "History": 88
}
largest=list(marks.values())[0]
for keys,values in marks.items():
    if values > largest:
        largest=values

print(largest)