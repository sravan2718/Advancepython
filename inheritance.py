
# multiple inheritance:

# creating class for father
class Dad():
	# writing a method for parent class 1
	def singing(self):
		print("Dad sings well")
		
# creating a class for mother
class Mom():
	# method for parent class 2
	def coding(self):
		print("Mom codes well")

# creating derived class
class Child(Dad, Mom):
	def play(self):
                print("Kid loves to play")
                
# creating object of the new derived class
child = Child()
# calling methods of parent classes and derived class
child.singing()
child.coding()
child.playing()

# example:

class Person:
	def display(self):
		print("Person called")
	
class Father(Person):
	def display(self):
		print("Father called")
	
class Mother(Person):
	def display(self):
		print("Mother called")
	
class Child( Mother, Father):
	pass
	
child_obj = Child()
child_obj.display()

#example;

class Car():
	def audi(self):
		print("This is an audi car")
	
class Bike():
	def kawasaki(self):
		print("This is a Kawasaki Ninja")
		
class Bus():
	def bharatBenz(self):
		print("This is Bharat Benz")
		
class Truck():
	def eicher(self):
		print("Eicher Truck here")
	
class Plane():
	def omanAir(self):
		print("Oman air all the way")
		
# derived classs with multiple base classes - Car, Bike, Bus, Truck, Plane
class Transport(Car, Bike, Bus, Truck, Plane):
	def main(self):
		print("Main class")

# creating derived class object
obj = Transport()
# calling funcions of base classes
obj.audi()
obj.kawasaki()
obj.bharatBenz()
obj.eicher()
obj.omanAir()
obj.main()

#example:

class Father():
    def Driving(self):
        print("Father loves Driving")
class Mother():
    def Cooking(self):
        print("Mother loves Cooking")
class Child(Father, Mother):
    def Playing(self):
        print("Child enjoying Playing")
c = Child()
c.Driving()
c.Cooking()
c.Playing()

#heirechal inheritance:

# Here, we will create the Base class   
class Parent1:  
    def func_1(self):  
        print ("This function is defined inside the parent class.")  
  
# Derived class1  
class Child_1(Parent1):  
    def func_2(self):  
        print ("This function is defined inside the child 1.")  
  
# Derivied class2  
class Child_2(Parent1):  
    def func_3(self):  
        print ("This function is defined inside the child 2.")
# Driver's code  
object1 = Child_1()  
object2 = Child_2()  
object1.func_1()  
object1.func_2()  
object2.func_1()
object2.func_3()

# Example:
    
class ClassA:
    def display(self):
        print('In Class A')

class ClassB(ClassA):
    def display(self):
        ClassA.display(self)
        print('In Class B')

class ClassC(ClassA):
    def display(self):
        ClassA.display(self)
        print('In Class C')

class ClassD(ClassA):
    def display(self):
        ClassA.display(self)
        print('In Class D')

x = ClassB()
y = ClassC()
z = ClassD()
x.display()
y.display()
z.display()

# example:

class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()

#example:

class A:
    def display(self, output):
        print(output)
        
class B(A):
    def display(self):
        super().display('Hello from B')
        
class C(A):
    def display(self):
        super().display('Hello from C')
        
b = B()
b.display()

c = C()
c.display()

# hybrid inheritance:

class A:
    def display(self):
        print("Super Parent display method")


""" class B used as intermediate class
to call class A's display method """
class B(A):
    def display(self):
        super().display()

''' child classes '''
class C(B):
    def display(self):
        super().display()
        print("Class C display method")
        
class D(B):
    def display(self):
        super().display()
        print("Class D display method")

c = C()
c.display()

d = D()
d.display()

# hybrid inheritance example
 
class parent1:                            # first parent class
    def func1(self):                   
        print("Hello Parent")
 
 
class parent2:                            # second parent class
    def func2(self):                   
        print("Hello Parent")
 
class child1(parent1):                    # first child class
    def func3(self):                   
        print("Hello Child1")
class child2(child1, parent2):            # second child class
    def func4(self):                   
        print("Hello Child2")   
                               
 
# Driver Code
test1 = child1()                          # object created
test2 = child2()
 
test1.func1()                       # child1 calling parent1 method
test1.func3()                       # child1 calling its own method
 
test2.func1()                       # child2 calling parent1 method
test2.func2()                       # child2 calling parent2 method
test2.func3()
test2.func4()


# Hybrid Inheritance
class vehicle:
    
    def __init__(self,model,mileage,price):
        self.price = price
        self.mileage = mileage
        self.model = model
        
    def show_details(self):
        print(f'Model : {self.model}')
        print(f'Price : {self.price}')
        print(f'Mileage : {self.mileage}')
class bike(vehicle):
    
    # Inherit Properties and Override
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.cc = cc
        self.tyre = tyre
    
    # Inherit Behavior and Override
    def show_details(self):
        super().show_details()
        print(f'CC : {self.cc}')
        print(f'Tyres : {self.tyre}')
    
    # Method of Derived Class
    def rating(self):
        print('4 star')
        

class car(bike,vehicle):
    
    def rating(self):
        print('5 star')

bajaj = bike("Dominar",40,145000,2,500)
tata = car("Safari",25,2500000,4,2000)

bajaj.show_details()
tata.show_details()

bajaj.rating()
tata.rating()
 


