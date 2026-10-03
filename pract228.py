
import pandas as pd

data = {
    "Name": ["Arjun", "Rohan", "Priya"],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)
print(df)

print(df["Name"])

print(df["Marks"])