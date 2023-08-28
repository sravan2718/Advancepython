
# In the following example,we have created the object of person class:

class Person:         
    name = "John"      
    age = 24  
    def display (self):      
        print("Age: %d \nName: %s"%(self.age,self.name))      
# Creating a emp instance of Employee class    
per = Person()      
per.display()     


# we have created object of the class:

# Creating a class named Scaler
class Scaler:
  a = 10
  b = 25
  c = 50

# Creating an object named "obj1", "obj2" & accessing the class properties(attributes).

obj1 = Scaler()
print(obj1.a)
print(obj1.b)

obj2 = Scaler()
print(obj2.c) 


#example:we will create a method in scalar class and excute it on the object:

# Creating a class named Scaler
class Scaler:
  def __init__(self, name, age, hobby):
    self.name = name
    self.age = age
    self.hobby= hobby

  def new(self):
    print("Heyy my name is " + self.name + ". I Love " + self.hobby)

obj2 = Scaler("Vikram", 24, "coding")
obj2.new()

# object property by changing the attribute value:

# Creating a class named Scaler
class Scaler:
  a = 10

# Declaring an object
obj1 = Scaler()
print(obj1.a)

#Modifying value
obj1.a = 200
print("After modifying the object properties")
print(obj1.a)

# the string representation of the object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

#insert a function and excute it on object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print(p1)

# create multiple objects:

# define a class
class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


