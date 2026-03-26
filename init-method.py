class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Buddy", 3)
print(d1.name, d1.age)
d1.bark()