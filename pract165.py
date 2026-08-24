#update old disease with new disease
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
        "Disease": "Headache"
    }
}

id = int(input("Enter patient id "))
new_disease = input("Enter  new  disease ")

for key ,value in patients.items():
    if id == key:
        value["Disease"]=new_disease
        break
else:
    print("invalid patient ID")

print(patients)
