"""
#local variables
def start_ultron():
    status = "ONLINE"
    print(status)
start_ultron()

#global variables
ultron_name = "ULTRON"
def show_name():
    print(ultron_name)
show_name()

#local vs global
name = "ULTRON"  #Global variable
def assistant():
    command = "Status"  #Local variable
    print(name)
    print(command)
assistant()

#Same variable name
status = "OFFLINE"
def Ultron():
    status = "ONLINE"
    print(status)
Ultron()
print(status)

#Global keyword
status = "OFFLINE"#global variable
def activate_ultron():
    global status #it is used to change the global variable value 
    status = "ONLINE"#globalvariable is changed 
activate_ultron()
print(status)    
"""
#Day - 8 project
#build Ultron status system
print("      Ultron System      ")
status = "OFFLINE"
battery = 100
def activate_ultron():
    global status
    status = "ONLINE"
    print("Ultron activate")
    print("status" , status)
def check_status():
    print("Ultron status: ", status)
    print("Battery : ", battery , "%")
def shutdown_ultron():
    global status
    status = "OFFLINE"
    print("Ultron Shutting down... ")
    print("status:", status)
activate_ultron() 
check_status()
shutdown_ultron()
check_status()
            
