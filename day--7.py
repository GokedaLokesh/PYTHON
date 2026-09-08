"""# function
def greet():
    print("Hello Lokesh")
greet()
# functions with parameters
def greet(name):
    print("Hello", name)
greet("Lokesh")
greet("Tony")

#multiple parameters
def add(a,b):
    print(a + b)
add(10,20)

#ex -2
def introduce(name,age):
    print("My name is", name)
    print("I am", age, " Years old")
introduce("Lokesh",19)

#return values
def add(a,b):
    return a + b
result = add(10,20)
print(result)
#second example
def square(number):
    return number * number
result = square(5)
print(result)    
#default parameters
def greet(name = "user"):
    print("hello", name)
greet()
greet("lokesh")
"""
#day-7 project
print("     ULTRON ASSISTANT DAY7   ")
#GREETING FUNCTION
def greet(name):
    return f"Hello {name} I am ULTRON."
#2.additon
def add(a,b):
    return a + b
#3 subtraction        
def sub(a,b):
    return a - b
    #multiplication

def mul(a,b):
    return a * b
    # divide

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b 
        # age checker
def check_age(age):
    if age >= 18:
        return "Access granted"
    else:
        return "Access denied" 
# 7 Ultron status
def ultron_status():
    return "All systems are operational " 
#main Program
name = input("ULTRON : WHAT IS YOUR NAME ?")
print(greet(name))
print("      Ultron calculator     ") 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 
print("Addition", add(num1,num2))
print("subtraction", sub(num1,num2))  
print("Multiplication", mul(num1,num2))
print("Division", div(num1,num2))  
print(" Security check")
age = int(input("enter your age: "))           
print(check_age(age))
print("\n----- System Status------")
print(ultron_status())