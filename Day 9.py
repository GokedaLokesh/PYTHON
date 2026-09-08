"""#Basic list 
numbers = [1,2,3,4,5]
squares = [n * n for n in numbers]
print(squares)

#with condition
numbers = range(1,11)
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# with if else
numbers = range(1,11)
result = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(result)

#day -9 mini project
print("    ULTRON DATA PROCESS  ")
numbers = list(range(1,21))
even_numbers = [n for n in numbers if n % 2 == 0]
squares = [n * n for n in numbers]
large_numbers = [n for n in numbers if n > 10]
print("Numbers", numbers)
print("Even numbers", even_numbers)
print("Squares", squares)
print("Greater than 10 ", large_numbers)
"""
#Day-9 Challenge
print("   ULTRON COMMAND SYSTEM     ")
commands = [ "hello",
             "status",
             "calculator",
             " weather",
             "music",
             "security",
             "exit"
             ]
# commands with more than 5 char
long_commands = [command for command in commands if len(command) > 5]
# convert all commands into uppercase
uppercase_commands = [command.upper() for command in commands]
# commands starts with s 
s_commands = [command for command in commands if command.startswith("s")]
#add Ultron before every command
ultron_commands = [f"ULTRON -> {command}" for command in commands]
print("\nORIGINAL COMMANDS")
print(commands) 
print("\ncommands with more than 5 char")
print(long_commands)
print("\n convert all commands into uppercase")
print(uppercase_commands)
print("\ncommands starts with s")
print(s_commands)
print("\n Ultron commands ")
for command in ultron_commands:
    print(command)
