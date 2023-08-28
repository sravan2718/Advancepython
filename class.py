# create a classed named person:

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("john", 36)


print(p1.name)
print(p1.age)

#example:

class person:
    def __init__(self, sport, year):
        self.sport = sport
        self.year = year

p1 = person("cricket", 2000)

print(p1.sport)
print(p1.year)

#defined a function inside a python class:

# create a class

class room:
    length = 0.0
    breadth = 0.0


    # method to calculate area
    def calculate_area(self):
        print("area of room=",self.length * self.breadth)

# create object of room class:

study_room = room()

# assign values to all the attributes
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside a class
study_room .calculate_area()

#define a class:

class Bike:
    name = ""
    gear = 0

#create object of a class
bike1 = Bike()

#access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"name: {bike1.name}, gears: {bike1.gear}")

# program to create student class and get the details student:

class Student:
 def __init__(self):
  self.sid=123
  self.sname="sai"
  self.saddress="hyderabad"
 def display(self):
  print("Student id is:",self.sid)
  print("Student name is:",self.sname)
  print("Student address is:",self.saddress) 

s1=Student()
s2=Student()
s1.display()
s2.display()


