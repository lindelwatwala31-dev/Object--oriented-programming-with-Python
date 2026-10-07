#Attributes - data regarding objects
# Example 3 - this is limiting though
class Fruit:                                            #Fruit is the class
    def __init__(self):
        self.name = "apple"                             #name and colour are attributes, they are created using the "self" parameter
        self.colour = "red"
my_fruit = Fruit()                                      #my_fruit is a variable name
print(my_fruit.colour)                                  #calling the colour attribute


#Example 3.1
class Fruits:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
apple = Fruits("apple", "green")  
banana = Fruits("banana", "yellow")
kiwi = Fruits("kiwi", "green")  
print(banana.colour)
print("My fruit is an", apple.name) 
print("My fruit is", kiwi.colour)  


#Methods - are functions related to objects
class Clothes:
    def __init__(self, brand, typ):
        self.brand = brand
        self.type = typ
    def details(self):                                  #Detail is the method
        print("My clothing is a " + self.type +
              " from " + self.brand)  
jersey = Clothes("H&M", "jersey")
jersey.details()                                        #calling on the method

         

