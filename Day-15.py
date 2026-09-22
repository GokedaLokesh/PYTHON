"""
#python class
class MyClass:
    x = 5
print(MyClass)    

#creating your object
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

#delete p1
class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = MyClass("Lokesh" , 19)
del p1
print(p1)        

##multiple objects
class MyClass:
    x = 5
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)

#pass statements
class person:
    pass
    
#python __init__()method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("Lokesh", 19)
print(p1.name)
print(p1.age) 
           
#self parameters
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)
p1 = person("Lokesh", 19)
p1.greet()
"""
#accesing properties with self
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} ")
car1 = car("toyota", "carollo", "2020")
car1.display_info()        