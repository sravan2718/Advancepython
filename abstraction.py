

# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
    def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

#Python program to define   
# abstract class  
  
from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):

class Triangle(Polygon):   
  
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):
  def sides(self):   
      print("I have 4 sides")   
  
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()

k = Hexagon()   
K.sides()


class Square(llgm):
  length = 5
  def Area(self):
    return self.length * self.length 

class Circle(llgm):
  radius =4 
  def Area(self):
    return 3.14 * self.radius * self.radius


sq = Square() #object created for the class ‘Square’
cir = Circle() #object created for the class ‘Circle’

print("Area of a Square:", sq.Area()) #call to ‘calculate_area’ method defined inside the class ‘Square’
print("Area of a circle:", cir.Area())

       
