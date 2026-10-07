import pandas as pd
data = {
    "Name": ["Arjun", "Rohan", "Priya"],
    "Marks": [85, 72, 91],
    "City": ["Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)

#print(df[df["Marks"] > 80])

print(df[df["City"] == "Mumbai"])
