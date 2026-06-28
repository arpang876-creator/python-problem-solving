class students:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("hi", self.name, "your avg score is", total / len(self.marks))

s1=students("Bruce",[98,96,97])
s1.avg()