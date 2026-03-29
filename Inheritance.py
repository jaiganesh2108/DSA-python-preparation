class Person: #Parent class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

name = Person("bruce", "wayne")
name.printname()

class Student(Person): #Child class
    pass

student1 = Student("clark", "kent")
student1.printname()