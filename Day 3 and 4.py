
#comparsion operator
a = 10
b = 20
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

#logical operators
age = 19
has_id = False
print(age >= 18 and has_id)
#or
print(age >= 18 or has_iid)
#not
print(not has_id)

#if
temp = 35
if temp > 30:
    print("ULTRON:It is hot.")
#if else
age = int(input("Lokesh : enter your age"))
if age >= 18:
    print("ULTRON : You are an adult")
else:
    print("ULTRON : you are a minor")
    
#nested conditions
age = 17
has_id = True
if age >= 18:
    if has_id:
        print("ULTRON : Access granted")
    else:
        print("ULTRON : Id required")
else:
    print("ULTRON : Access denied")        
    
#ULTRON Assistant
print("        ULTRON Assistant       ")
name = input("ULTRON : What is your name: ")
age = int(input("ULTRON : How old are you: "))
print("/nChoose an Option: ")
print("1.Check age")
print("2.check weather")
print("3.Check access")
choice = input("Lokesh : ")
if choice == "1":
    if age >= 18:
      print("ULTRON : You are an adult")
    else:
      print("ULTRON : you are under 18")
elif choice == "2":
    temp = float(input("ULTRON :enter tempature"))
    if temp >= 35:
      print("ULTRON : It is hot.")
    elif temp >= 25:
         print("ULTRON : The weather is warm.")
    elif temp >= 15:
         print("ULTRON : The weather is cool.")
    else:
         print("ULTRON : It is cold.")
elif choice == "3":
    has_password = input("ULTRON : do you know the password : (yes/no): ")
    if age >= 18 and has_password == "yes":
         print("ULTRON : Access granr=ted.")
    else:
         print("ULTRON : Access denied.")
else:
     print("ULTRON : Invalid option.")
     
     print("ULTRON : Task Complected.")     