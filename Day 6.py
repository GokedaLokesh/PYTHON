"""
#list
commands = ["hello","time","weather","music","exit"]
print(commands)
#Tuple
assistant_info = ("ULTRON","1.0","PYTHON")
print(assistant_info)
#set
categories = {"basics","information","entertainment"}
print(categories)
#dictionary
command_database = {
    "hello" : "Hello Lokesh! How can I help you?",
    "time" : "Checking the current time...",
    "weather" : "Checking the weather...",
    "music" : "Opening music...",
    "exit" : "Shutting down Ultron..."
    }
print(command_database)
"""
#ULTRON ASSISTANT
print("     ULTRON ASSISTANT     ")
print("Command Database V1.0")
#list
commands = [
    "hello",
    "time",
    "weather",
    "music",
    "status",
    "exit"
    ]
#ultron info
ultron_info = (
    "ULTRON",
    "VERSION 1.0",
    "PYTHON" 
    )
#set
categories = {
    "basics",
    "information",
    "entertainment",
    "system"
    }
#dictionary
command_database = {
        "hello" : "Hello Lokesh! How can I help you?",
        "time" : "Checking the current time...",
        "weather" : "Checking the weather...",
        "music" : "Opening music...",
        "exit" : "Shutting down Ultron..."
        }
print("\nUltron information : ")
print("Name :",ultron_info[0])
print("Version :",ultron_info[1])
print("Language :",ultron_info[2])
print("\n Command Categories :")
print(categories)
while True:
    print("Available Commands")
    for command in commands:
        print("-", command)
    user_command = input("\nUser: ").lower()
    if user_command in command_database :
        print("ULTRON :" , command_database [user_command])
        if user_command == "exit":
            print("\n ULTRON : System shutdown complete")
            break
    else:
         print("ULTRON : I don't reconize that command.")

       