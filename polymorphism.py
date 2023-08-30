
# class polymorphism:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat

plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


# inheritance class polymorphism#

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")


car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


# for demonstrating the Polymorphism  
  
def add(p, q, r = 0):  
    return p + q + r  
  
# Driver code  
print (add(6, 23))  
print (add(22, 31, 544))

#polymorphism with function and object:

class Tomato(): 
     def type(self): 
       print("Vegetable") 
     def color(self):
       print("Red") 
class Apple(): 
     def type(self): 
       print("Fruit") 
     def color(self): 
       print("Red") 
      
def func(obj): 
       obj.type() 
       obj.color()
        
obj_tomato = Tomato() 
obj_apple = Apple()
func(obj_tomato) 
func(obj_apple)

# example:

class India():
     def capital(self):
       print("New Delhi")
 
     def language(self):
       print("Hindi and English")
 
class USA():
     def capital(self):
       print("Washington, D.C.")
 
     def language(self):
       print("English")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
country.capital()
country.language()

# example:

class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")

obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()

# example:

class Vehicle:
    def __init__(self, fare):
        self.fare = fare
    def __add__(self, other)://using the special function __add__ operator
        return self.fare+ other.fare

bus= Vehicle(20)
car= Vehicle(30)
total_fare=bus+ car
print(total_fare)

# overloading example:

class Vehicle:
    def __init__(self, fare):
        self.fare = fare
    def __lt__(self, other):// relational operator  __lt__ is used here as the special function
        return self.fare< other.fare

bus= Vehicle(10)
car= Vehicle(30)
compare=bus< car
print(compare)

# example:

p = 55
q = 77
r = 9.5
g1 = "Guru"
g2 = "99!"
print("the sum of two numbers",p + q)
print("the data type of result is",type(p + q))
print("The sum of two numbers",q + r)
print("the data type of result is", type (q + r))
print("The concatenated string is", g1 + g2)
print("The data type of two strings",type(g1 + g2))

# overloading and overriding:
from math
import pi
class square:
    def __init__(self, length):
    self.l = length
def perimeter(self):
    return 4 * (self.l)
def area(self):
    return self.l * self.l
class Circle:
ef __init__(self, radius):
    self.r = radius
def perimeter(self):
    return 2 * pi * self.r
def area(self):
    return pi * self.r * * 2
# Initialize the classes
sqr = square(10)
c1 = Circle(4)
print("Perimeter computed for square: ", sqr.perimeter())
print("Area computed for square: ", sqr.area())
print("Perimeter computed for Circle: ", 
c1.perimeter())
print("Area computed for Circle: ", c1.area())

# class methods:

lass baseclass:
    def __init__(self, name):
    self.name = name
def area1(self):
    pass
def __str__(self):
    return self.name
class rectangle(baseclass):
    def __init__(self, length, breadth):
    super().__init__("rectangle")
self.length = length
self.breadth = breadth
def area1(self):
    return self.length * self.breadth
class triangle(baseclass):
    def __init__(self, height, base):
    super().__init__("triangle")
self.height = height
self.base = base
def area1(self):
    return (self.base * self.height) / 2
a = rectangle(90, 80)
b = triangle(77, 64)
print("The shape is: ", b)
print("The area of shape is", b.area1())
print("The shape is:", a)
print("The area of shape is", a.area1())

# example:

class amazon:
    def __init__(self, name, price):
    self.name = name
self.price = price
def info(self):
    print("This is product and am class is invoked. The name is {self.name}. This costs {self.price} rupees.")
class flipkart:
    def __init__(self, name, price):
    self.name = name
self.price = price
def info(self):
    print(f "This is product and fli class is invoked. The name is {self.name}. This costs {self.price} rupees.")
FLP = flipkart("Iphone", 2.5)
AMZ = amazon("Iphone", 4)
for product1 in (FLP, AMZ):
    product1.info()