import csv
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

with open("C:/Users/Lenovo/.vscode/python/information.csv","r") as f:
    d = csv.DictReader(f)
    x=[]
    y=[]
    name = input("Enter Name")
    for i in d:
        if name == i["emp_name"]:
            with open("C:/Users/Lenovo/.vscode/python/salary.csv","r") as e:
                data = csv.DictReader(e)
                for j in data:
                    if name == j["emp_name"]:
                        y.append(float(j["salary"]))
                        x.append(int(j["year"]))

plt.plot(x, y, marker='o')
plt.xlabel("Year")
plt.ylabel("Salary")
plt.grid()
plt.show()


            

    