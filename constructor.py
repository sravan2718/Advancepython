

# instance variables:

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)


# example:
class student:
  # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# modify instance variable
stud.name = 'Emma'
stud.age = 15

print('After')
print('Name:', stud.name, 'Age:', stud.age)


#Access instance variable in the instance method:

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student("Jessa", 20)

# call instance method
stud.show()


# example:

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))


# example;

class Student:
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# add new instance variable 'marks' to stud
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)


# dynamacally delete instance variables:

class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
print(s1.name)

# example:

class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

    def show(self):
        print(self.roll_no, self.name)

s1 = Student(10, 'Jessa')
s1.show()

# delete instance variable using delattr()
delattr(s1, 'roll_no')
s1.show()

# access instance variable:

class Vehicle:
    def __init__(self):
        self.engine = '1500cc'

class Car(Vehicle):
    def __init__(self, max_speed):
        # call parent class constructor
        super().__init__()
        self.max_speed = max_speed

    def display(self):
        # access parent class instance variables 'engine'
        print("Engine:", self.engine)
        print("Max Speed:", self.max_speed)

# Object of car
car = Car(240)
car.display()


# python class method:

class Student:
  marks = 0

  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)

# convert compute_marks() to class method
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

#example:

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()


# example;

From datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()


# static variables:

class Bakery:
    type = 'cake'                  # Class Variable
    def __init__(self,flavor,price):
        self.flavor = flavor            # Instance Variable
        self.price = price            # Instance Variable
 
# Objects of Bakery class
a = Bakery('Butterscotch Cake', 300)
b = Bakery('Chocolate-Truffle Cake', 250)
 
print(a.type)  # prints "cake"
print(b.type)  # prints "cake"
print(a.flavor)    # prints "Butterscotch Cake"
print(b.flavor)    # prints "Chocolate-Truffle Cake"
print(a.price)    # prints "300"
print(b.price)    # prints "250"

# example:

class Cake:
  noOfCakes = 0
  
  
  @classmethod
  def show(cls):
    print('Inside class method')
    cls.noOfCakes = cls.noOfCakes + 1 ## accessing using clas
    print('No of cakes: ', cls.noOfCakes)
    Cake.noOfCakes = Cake.noOfCakes + 1 ##accessing using class name
    print('No of cakes: ', Cake.noOfCakes)
    
    
    
    c = Cake()
c.display()
c.show()
c.appear()

# example;

class Cake:
  noOfCakes = 0
  
  def __init__(self):
    type(self).noOfCakes = type(self).noOfCakes + 1
  
c1 = Cake() ##Object1
c2 = Cake()  ##Object2
print('Accessing class variable using object c1: ', c1.noOfCakes)
print('Accessing class variable using object c2: ',c2.noOfCakes)
print('Accessing class variable using classname: ', Cake.noOfCakes)

 
