class students:
    def __init__(self,name,marks,grade,team):
        self.name=name
        self.marks=marks
        self.grade=grade
        self.team=team
    
    def student_detail(self): #method used is abstractiion as its hidden from users
       print("name", self.name, "grade", self.grade, "got an marks of", self.marks, "and is in team",self.team)

team1="A"
team2="B"

s1=students("arpan",99,12,team1)
s1.student_detail()

s2=students("arnav",100,10,team2)
s2.student_detail()


class graduate(students):
    def __init__(self,name,marks,grade,team,stream):
        super().__init__(name,marks,grade,team)#calling parent class initializer
        self.stream=stream

    def student_detail(self):
        print("name", self.name, "grade", self.grade, "got an marks of", self.marks, "and is in team", self.team, "and stream", self.stream)

grad_s1=graduate("Ram",100,15,"C","Science")
grad_s1.student_detail()

#modify object
'''s1.marks=(97)
print(s1.marks)'''

#delete object
'''del s1.grade'''#throw an error as grade will be deleted


#There are 4 features in oops
#abstraction : Hidinng unecessary details from user through class and methods


#polymorphism : allows methods to have an same name but ive different outputs depending on the behaviour and conditions


#Inheritance : allows  one child class to reuse the properties of parent class


#Encapsulation : Restirict access to some of the attributes