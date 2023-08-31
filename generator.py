
def f1():
    yield "Sai"
    yield 123
    yield "SaiRam"
    yield 123.45

print(type(f1))
for i in f1():
    print(i)

def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Using the generator in a loop
print(type(countdown))
for num in countdown(5):
    print(num)


even_numbers = [x for x in range(10) if x % 2 == 0]

print(type(even_numbers))
for i in even_numbers:
    print( i)

#There's another type of generator called a generator expression, which is similar to a list
#comprehension but creates a generator on-the-fly.
#for example:

even_numbers = (x for x in range(10) if x % 2 == 0)

print(type(even_numbers))
for i in even_numbers:
    print( i)


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
    
# A Python program to demonstrate use of
# generator object with next()
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
 
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x)) 

  A simple generator for Fibonacci Numbers
def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object
x = fib(5)
 
# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
 
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)


def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

 def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

 def mygenerator():
    print('First item')
    yield 10

    return

    print('Second item')
    yield 20

    print('Last item')
    yield 30  