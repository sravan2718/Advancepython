
# first, we will create the base class  
class Base1:  
    def __init__(self):  
  
        # the protected member  
        self._p = 78  
  
# here, we will create the derived class  
class Derived1(Base):  
    def __init__(self):  

# now, we will call the constructor of Base class  
        Base1.__init__(self)  
        print ("We will call the protected member of base class: ",  
            self._p)  
  
# Now, we will be modifing the protected variable:  
        self._p = 433  
        print ("we will call the modified protected member outside the class: ",  
            self._p)  
  
  
obj_1 = Derived1()  
  
obj_2 = Base1()  
  
# here, we will call the protected member  

Example:

class Base1:  
    def __init__(self):  
          self.p = "Javatpoint"  
          self.__q = "Javatpoint"  
  
# Creating a derived class  
class Derived1(Base1):  
      def __init__(self):  
  
# Calling constructor of  
# Base class  
     Base1.__init__(self)  
     print("We will call the private member of base class: ")  
     print(self.__q)  
  
  
# Driver code  
obj_1 = Base1()  
print(obj_1.p)

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print("Name: ", emp.name, 'Salary:', emp.salary)

# calling public method of the class
emp.show()

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp.__salary)

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)
 Run
O
