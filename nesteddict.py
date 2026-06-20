dict={
    "Student": "Arpan",
    "marks": {
        "math": 90,
        "science": 85,
        "english": 88
    }
}
print(dict["Student"])
print(dict.get("marks").get("math"))
print(dict["marks"]["math"])# Print the value of the key "math" in the nested dictionary
print(dict.keys())# Print the keys in the dictionary
print(dict.values())
print(dict.items())
