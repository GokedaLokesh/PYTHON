"""#create and write to a file
file = open("ultron.txt", "w")
file.write("Hello! I am ULTRON \n")
file.write("I am learning python file handling")
file.close()
print("ULTRON : Data saved succesfully")
#read a file
file = open("ultron.txt", "r")
data = file.read()
print(data)
file.close()
#append to a file
file = open("ultron.txt", "a")
file.write("\nDay 11: I have learned file handling")
file.close()
print("ULTRON : New memory added")
#bet practice with open()
with open("ultron.txt", "r") as file:
    data = file.read()
    print(data)
    """
    # day 11 mini project
print("     ULTRON MEMORY SYSTEM   ")
memory = input("ULTRON : ENTER A MEMORY")
#SAVE MEMORY
with open("ultron_memory.txt", "a") as file:
    file.write(memory + "\n")
print("\n Ultron : REading  memories...")
with open("ultron_memory.txt", "r") as file:
    memories = file.read()
    print(memories)
    print("ULTRON : MEMORY SYSTEM COMPLETED")