#decorator:

def extra_msg(printmsg):
    def inner(name):
        if name=="Raju":
            print("HEllo",name,"Good Evening")
        else:
            printmsg(name)
    return inner

@extra_msg
def printmsg(name):
    print("hello",name,"Good Morning")

printmsg("Balaji")
printmsg("sravan")
printmsg("mani")


# example:

def mydiv(div):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return div (x,y)
    return inner
@mydiv
def div(a,b):
    return (a/b)

print(div(6,2))
print(div(2,6))

# example;

def my_decorator(func):
    def greet():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return greet

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# example;

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("sravan")

#timing a function;


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(3)
    print("Function completed.")

slow_function()






