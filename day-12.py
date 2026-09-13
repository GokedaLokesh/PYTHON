"""
#json example
{
  "name" : "Lokesh",
  "age" : 19,
  "language" : "python"
}
#json vs python dictionary
person = {
  "name" : "Lokesh",
  "age" : 19
}
print(person)
#import json module
import json
print("json module impored succesfully")

#simple json data
import json
student = {
    "name" : "Lokesh",
    "age" : 19,
    "course" : "Python",
    "complected" : True
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])

#json with lists
student = {
  "name" : "Lokesh",
  "skills" : [
       "python",
       "ai",
       "machine learning"
  ]
}
print(student)
print(student["skills"])
print(student["skills"][0])
#multiple statements
students = [
  {
    "name" : "Lokesh",
    "age" : 19
  },
  {
    "name" : "u",
    "age" : 19
  },
  {
    "name" : "us",
    "age" : 19
  },
  {
    "name" : "usa",
    "age" : 19
  }
]
print(students)
print(students[0])
print(students[0]["name"])

#json_dumps
import json
person = {
  "name" : "lokesh",
  "age" : 19,
  "skill" : "python"
}
json_data = json.dumps(person)
print(json_data)
#make more readable
json_data = json.dumps(person, indent = 4)
print(json_data)
#json loads
import json
json_data = '{"name" : "Lokesh", "age" : 19}'
person = json.loads(json_data)
print(person)
print(person["name"])
print(person["age"])
"""
#create a json file
import json
person = {
  "name" : "Lokesh",
  "age" : 19,
  "skills" : [
    "python",
    "ai",
    "ml"
  ]
}
with open("person.json", "w") as file:
  json.dump(person, file, indent = 4)
  print("json file created")
  #read the json file
  
with open("person.json", "r") as file:
  person = json.load(file)
  print(person)
  print("name : ", person["name"])
  print(person["age"])
  print(person["skills"])
  #update json data
  person["age"] = 22
  print(person)
  with open("person.json", "w") as file:
    json.dump(person, file, indent = 4)
  print("data updated")  
  #addnew information
  person["city"] = "Hyderabad"
  print(person)
  with open("person.json", "w") as file:
    json.dump(person, file, indent = 4)
    #new skill
  person["skills"].append("deep learning") 
  print(person["skills"])
with open("person.json", "w") as file:
  json.dump(person, file, indent = 4)