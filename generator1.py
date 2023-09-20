# generators;

def simple_generator():
    yield 2
    yield 4
    yield 6

gen = simple_generator()

for value in gen:
    print(value)

# example;


gen = (x for x in range(1, 6))

for value in gen:
    print(value)


#example;

def fun1(x):
    print("I am in function1 and x value is",x)
def fun2():
    print(" i am in function2")

def fun3(function):
    print("i am in function3")
    function()
def func4(function,x):
    print("i am in function4")
    function(x)

#fun3(fun2)
func4(fun1,50)

#another example;

def outer():
    print("i am in outer function")
    def display():
        print("this is display function")
    display()

outer()

# another example;

def display():
    a=10
    b=20
    yield a+b
    a=100
    b=200
    yield  a+b
    a=1000
    b=2000
    yield a+b

   
result=display()
print(result)
print(next(result))
print(next(result))
print(next(result))


for result in display():
    print("Result=",result)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator in a loop
print(type(countdown))
for num in countdown(5):
    print(num)

def f1():
    yield "sravan"
    yield 231
    yield "Sravan"
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
for num in countdown(3):
    print(num)


even_numbers = [x for x in range(10) if x % 2 == 0]

print(type(even_numbers))
for i in even_numbers:
    print(i)


def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

gen = infinite_counter()

for i in range(5):
    print(next(gen))


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()

for i in range(10):
    print(next(gen))

