"""
 #for Loop
for i in range(5):
  print("ULTRON is running... ")
#range
range(5)
print(range)
#for ex2
for i in range(5):
  print("ULTRON : System scan", i+1)
  #range (start ,stop)
  for i in range(1,6):
      print(i)
      for i in range(0,11,2):
          print(i)
          #while loop
          count = 5
          while count <= 5:
              print("ULTRON :", count)
              count += 1
              """
# today task
print("ULTRON ONLINE")
while True:
    command = input("\nLokesh :Enter your command ").lower()
    if command == "hello":
        print("ULTRON : Hello Lokesh! how can I help you?")
    elif command == "status":
        print("ULTRON : All systems are operational.")
    elif command == "count":
        number = int(input("ULTRON : count upto : "))
        for i in range(1,number + 1):
            print("ULTRON :", i)
    elif command == "exit":
        print("ULTRON : Shutting down...")
        break
    else:
        print("ULTRON :I don't understand that command:")
        print("ULTRON : System offline")       
            
                      