"""
#Basic example
try:
    age = int(input("ULTRON : ENTER YOUR AGE:"))
    print("your age is :", age)
except ValueError:
    print("ULTRON :  please enter a valid number")
    """
#day 10 project
def process_command(command):
    if command == "hello":
        print("ULTRON : hello Lokesh! how can I help you? ")
    elif command == "status":
        print("ULTRON : All systems are operational")
    elif command == "calculator":
        try:
            num1 = float(input(" ULTRON : enter first number"))
            operator = input("ULTRON : enter operator (+,-,*,/):")
            num2 = float(input(" ULTRON : enter second  number"))
            if operator == "+":
                print("Result:", num1 + num2)
            
            elif operator == "-":
                print("Result:", num1 - num2)
             #" ULTRON : enter second  number"))
            elif operator == "*":
                print("Result:", num1 * num2) 
             #" ULTRON : enter second  number"))
            elif operator == "/":
                print("Result:", num1 / num2)   
            else:
                print("ULTRON : Invalid operator")
        except ValueError:
            print("Ultron : please enter valid numbers")
        except ZeroDivisionError:
            print("Ultron : Cannot divide by zero")
    elif command == "exit":
        return False
    else:
        print("ULTRON : UNKNOWN COMMAND")
        return True
print("ULTRON ASSISTANT")
print("error handling V1.0")
commands = [
    "hello",
    "status",
    "calculator",
    "exit"
          ]
while True:
    command = input("\nuser: ").lower().strip()
    try:
        running = process_command(command)
        if running is False:
            print("ULTRON : SHUTTING DOWN...")   
            break
    except Exception as error:
        print("ULTRON : something went wrong")
        print("ULTRON : error handled succesfully")
        print("error:", error)               
                                            
        
                
