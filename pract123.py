marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}
highest = 0
subject = ""
for keys,values in marks.items():
    if values > highest:
        highest = values
        subject = keys
print("Highest marks",subject,":",highest)
