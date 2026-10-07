#Class
class Student:                                          #Example, Student must start with a capital letter
    def __init__(self):                                 #self is the parameter
        self.name = "Linda"                             # Name, age and marks are attributes       
        self.age = 20
        self.marks = 80
    
    def talk(self):                                     # Talk is the action
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)
        
s1 = Student()                                          # s1 is the object/ method and Student is class        
print(s1.name)
s1.talk()                                               # We are calling on the action of talk and it is known as instance method

s1.name = "Bellsy"
print(s1.name)

s2 = Student()
print(s2.name)

# Init method
#Example 1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

account = BankAccount("Alice", 100)
print(account.owner)                                # Alice
print(account.balance)                              # 100

# Example 3
class Cinema:                                          #Example, Student must start with a capital letter
    def __init__(self, movie, time, room):
        self.movie = movie                             # Movie, time, and room are attributes       
        self.time = time
        self.room = room

showing = Cinema("Ice Age",f"13pm", 8)
print("Movie:",showing.movie)                                   
print("Cinema room:",showing.room) 

#Example 4
n = input("Name: ")
a = int(input("Age: "))
m = int(input("Marks: "))

class Student:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m
    def display(self):
        print(f"My name is", self.name, "and I am", self.age,"years old and I got", self.marks ,"out of 100")  

s1 = Student(n, a, m)
s1.display()                              #You need to call the method/ action

#Adding a default value if you don't want to input anything
class Student:
    def __init__(self, n, a, m=0):                  # m=0 is a default value
        self.name = n
        self.age = a
        self.marks = m
    def display(self):
        print("My name is", self.name)
        print("I am", self.age,"years old")
        print("I got",self.marks ,"out of 100")  

s1 = Student("Linda", 22)
s1.display()                              #You need to call the method/ action

#Adding multiple arguments
class Student:
    def __init__(self, n, a, *m):                  # m=0 is a default value
        self.name = n
        self.age = a
        self.marks = m
    def display(self):
        print("My name is", self.name)
        print("I am", self.age,"years old")
        print("I got",self.marks ,"out of 100")  

s1 = Student("Linda", 22, 40, 30, 90)
s1.display()                              #You need to call the method/ action

#Want to pass keyword arguments
class Student:
    def __init__(self, n, a, **m):                  # m=0 is a default value
        self.name = n
        self.age = a
        self.marks = m
    def display(self):
        print("My name is", self.name)
        print("I am", self.age,"years old")
        print("I got",self.marks ,"out of 100")  

s1 = Student("Linda", 22, english = 40, science = 30, maths = 90)
s1.display()                              #You need to call the method/ action

print("------------------------")

s2 = Student("Zoe", 45, english = 90, science = 70, maths = 65)
s2.display()                              #You need to call the method/ action


                     