student = {
    "Name": "Arpan",
    "Age": 20,
    "City": "Mumbai",
    "Course": "Python"
}

word =input("Enter any key:")
for key in student:
    if word == key:
        del student[key]
        print(student)
        break
    else:
        print("Key doesn't exist")
        break