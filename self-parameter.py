class Example():
    a = 10
    def add(self, a):
        self.a = a #this will create an instance variable a that shadows the class variable a

exc = Example()
print(exc.a)
exc.add(20)
print(exc.a)
print(Example.a) #class variable a is still 10, instance variable a is 20

""" Instructions
Inside the editor, complete the following steps:
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1"""
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)

c1 = Car("Ford")
c1.show()