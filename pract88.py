employee = {
    "name": "Arpan",
    "salary": 50000,
    "department": "IT"
}

print(employee.values())
employee['salary']=60000
employee['experience']=2
del employee['department']
print(employee)