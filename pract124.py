#Lowest marks
marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}

lowest = 100
subject = "" 
for key, values in marks.items():
    if values < lowest:
        lowest =values
        subject =key
print("Subject with lowest marks",subject,lowest)