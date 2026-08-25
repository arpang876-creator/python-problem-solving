patients = {
    101: {
        "Name": "Arpan",
        "Age": 20,
        "Disease": "Fever"
    },
    102: {
        "Name": "Rahul",
        "Age": 35,
        "Disease": "Cold"
    },
    103: {
        "Name": "Priya",
        "Age": 28,
        "Disease": "Fever"
    }
}

disease = input("Enter the disease name")

for key,value in patients.items():
    if disease == value["Disease"]:
        print(value)
else:
    print("Disease not found")
        

