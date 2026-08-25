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

patient_id=int(input("enter the patient id"))
name = input("Enter the name")
age = int(input("Enter the age"))
disease = input("Enter disease")

patients[patient_id]={
    "Name" : name,
    "Age" : age,
    "Disease" : disease
}

print(patients)