#Multiple constructors in Python - can anly use one constructor
class Student:
    def __init__(self, n):
        self.name = n
    def display(self):
        print("Hi", self.name)

s1 = Student("Shanny")
s1.display()

#The self parameter, you can use another name = cls
class Student:
    def __init__(cls, n):
        cls.name = n
    def display(cls):
        print("Hi", cls.name)

s1 = Student("Hardy")
s1.display()