dict={'name':'Arpan',
     'age':20,
    'city':'Mumbai'}

print(dict['city'])


dict['number']=7506589580

print(dict)

dict['name']='Arnav'
print(dict)

for keys,values in dict.items():
    print(keys,":",values)
