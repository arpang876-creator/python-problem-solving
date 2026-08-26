#Max age of a patient

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

highest = 0
name = ""
for key,value in patients.items():
    if int(value["Age"]) > highest:
        highest = int(value["Age"])
        name = value["Name"]
print("Maximum age is: ",name , highest)
    
    