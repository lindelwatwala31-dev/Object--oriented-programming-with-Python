class Student:                                          #Example, Student must start with a capital letter
    def __init__(self):
        self.name = "Linda"                             # Name, age and marks are attributes       
        self.age = 20
        self.marks = 80
    
    def talk(self):                                     # Talk is the action
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)
        
s1 = Student()                                          # s1 is the object/ method and Student is class        
print(s1.name)
s1.talk()                                               # We are calling on the action of talk

s1.name = "Bellsy"
print(s1.name)

s2 = Student()
print(s2.name)