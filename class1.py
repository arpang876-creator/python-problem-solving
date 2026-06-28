class students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")


s1 = students("Arpan",100)
print(s1.name,s1.marks)

s2 = students("Arnav",98)
print(s2.name,s2.marks)