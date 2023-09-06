
# paramaterized constructor:

class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
  
# accessing display() method to print employee 1 information  


emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display()  


# example:

class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    


#python non paramaterized constructor:

class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()  
student.show("John")

# example:

class Student:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()


#python default constructor:

class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()

# example:

class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
  
st = Student()


# example:

class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
    # creates the object of the class Student  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23  
setattr(s, "age", 23)  

# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)


# example:


class Student:    
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    
s = Student("John",101,22)    
print(s.__doc__)    
print(s.__dict__)    
print(s.__module__)    

# default constructor:


class A():
    check_value = 1000
    # a method
    def value(self):
        print(self.check_value)

# creating an object of the class
obj = A()

# calling the instance method using the object
obj.value()

# example:

class Family:
   members = 10
   def __init__(self, count):
      self.members = count
   
   def disply(self):
      print("Number of members is", self.members)  

joy_family = Family(25)
joy_family.disply()

# example:

class Player:
   def __init__(self):
      self.position = 0
   
   # Add a move() method with steps parameter     
   def move(self, steps):
      self.position = steps
      print(self.position)
   
   def result(self):
      print(self.position)

player1 = Player()
print('player1 results')
player1.move(2)
player1.result()

print('p2 results')
p2 = Player()
p2.result()



# example:


class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane()

# example:


class Bug:
   def __init__(self):
       self.wings = 4

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
tom = Bug()

print(tom.wings)
print(bob.arms)

# example:


class Employee:
   def __init__(self, id,name):
       self.id=id
       self.name=name
   def display(self):
       print("Hello my id is :", self.id)
       print("My name is :", self.name)
e1=Employee(1, 'Nithin')
e1.display()
e2=Employee(2, 'Arjun')
e2.display()

# example:

class Student:
  def __init__(self, name, roll_no)
    self.name = name
    self.roll_no = roll_no

  def display(self):
    print ("Roll No.: %d \nName: %s" % (self.roll_no, self.name))

# Creating object of the class
stud1 = Student("Alex", 34)
stud2 = Student("Mark", 67)

stud1.display()
stud2.display()


# example:

class Student:

# Parameterized constructor
  def __init__(self, name, roll_no):
    self.name = name
    self.roll_no = roll_no

  def display(self):
    print ("Roll No.: %d \nName: %s" % (self.roll_no, self.name))

# Creating object of the class
stud1 = Student("Navya", 34)
stud2 = Student("Mia", 67)

stud1.display()
stud2.display()
