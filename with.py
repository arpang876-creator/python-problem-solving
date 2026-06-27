#read
'''with open("demo1.txt","r") as f:
    data = f.read()
print(data)
    f.close()    '''

#overwrite
'''with open("demo1.txt", "w") as f:
    data = f.write( "My name is Arpan Ghosh")
    f.close()'''

#append

with open("demo1.txt", "a") as f:
    data = f.write("Greatest of all time")
f.close()





