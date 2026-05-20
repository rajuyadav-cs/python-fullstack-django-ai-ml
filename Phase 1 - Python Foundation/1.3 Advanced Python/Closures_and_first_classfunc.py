# closures_and_first_class_functions.py


# ==========================================================
# FIRST-CLASS FUNCTIONS
# ==========================================================

# in python functions are treated like normal objects

# this means:
#
# - functions can be stored in variables
# - functions can be passed as arguments
# - functions can be returned from other functions


print("\n==============================")
print("FUNCTION AS VARIABLE")
print("==============================\n")


def greet():

    print("Hello from greet function")


# storing function in variable
x = greet

# calling through variable
x()

# important:
# x = greet
# means function reference stored
#
# x = greet()
# means function executes immediately


print("\n==============================")
print("FUNCTION AS ARGUMENT")
print("==============================\n")


def say_hello():

    print("Hello")


def execute_function(func):

    print("Before function call")

    func()

    print("After function call")


# passing function as argument
execute_function(say_hello)


print("\n==============================")
print("FUNCTION RETURNING FUNCTION")
print("==============================\n")


def outer():

    print("Outer function executed")

    def inner():

        print("Inner function executed")

    return inner


# outer returns inner function
returned_function = outer()

# now calling returned inner function
returned_function()


print("\n==============================")
print("NESTED FUNCTIONS")
print("==============================\n")


def parent():

    print("Parent function")

    def child():

        print("Child function")

    child()


parent()


print("\n==============================")
print("BASIC CLOSURE")
print("==============================\n")


# closure means:
# inner function remembers variables
# from outer function


def outer_function():

    message = "Hello from closure"

    def inner_function():

        # inner function can access outer variable
        print(message)

    return inner_function


closure_func = outer_function()

# outer function already finished
# but inner function still remembers message
closure_func()


print("\n==============================")
print("ANOTHER CLOSURE EXAMPLE")
print("==============================\n")


def create_greeting(name):

    def greeting():

        print(f"Hello {name}")

    return greeting


g1 = create_greeting("Raju")
g2 = create_greeting("Aman")

g1()
g2()

# each returned function remembers its own data


print("\n==============================")
print("CLOSURE WITH PARAMETERS")
print("==============================\n")


def multiplier(x):

    def multiply(y):

        return x * y

    return multiply


# creating special functions
double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))

# double remembers x = 2
# triple remembers x = 3


print("\n==============================")
print("COUNTER USING CLOSURE")
print("==============================\n")


def counter():

    count = 0

    def increment():

        # without nonlocal python creates new local variable
        nonlocal count

        count += 1

        print("Current count:", count)

    return increment


c = counter()

c()
c()
c()

# count value is preserved between calls


print("\n==============================")
print("WHY nonlocal IS IMPORTANT")
print("==============================\n")


def test():

    value = 10

    def update():

        nonlocal value

        value += 5

        print(value)

    return update


t = test()

t()
t()

# nonlocal allows modifying outer variable


print("\n==============================")
print("WITHOUT nonlocal")
print("==============================\n")


def demo():

    num = 1

    def change():

        # this creates new local variable
        # if we try:
        #
        # num += 1
        #
        # python gives error

        print("Cannot modify outer variable without nonlocal")

    return change


d = demo()

d()


print("\n==============================")
print("CLOSURE STATE PRESERVATION")
print("==============================\n")


def bank_account(balance):

    def deposit(amount):

        nonlocal balance

        balance += amount

        print("Balance after deposit:", balance)

    return deposit


account = bank_account(1000)

account(500)
account(300)

# balance is remembered by closure


print("\n==============================")
print("FIRST-CLASS FUNCTION IN LIST")
print("==============================\n")


def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


# storing functions inside list
operations = [add, subtract, multiply]

for operation in operations:

    print(operation(10, 5))


print("\n==============================")
print("FIRST-CLASS FUNCTION IN DICT")
print("==============================\n")


functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}

print(functions["add"](5, 2))
print(functions["multiply"](5, 2))


print("\n==============================")
print("CLOSURE INSIDE LOOP")
print("==============================\n")


def power_creator(power):

    def calculate(number):

        return number ** power

    return calculate


square = power_creator(2)
cube = power_creator(3)

print(square(4))
print(cube(4))


print("\n==============================")
print("CHECKING CLOSURE")
print("==============================\n")


def outer():

    x = 100

    def inner():

        print(x)

    return inner


f = outer()

# closure stores outer variables internally
print(f.__closure__)

f()


print("\n==============================")
print("REAL PROJECT STYLE EXAMPLE")
print("==============================\n")


# simple logger using closure

def logger(prefix):

    def log(message):

        print(f"[{prefix}] {message}")

    return log


info_logger = logger("INFO")
error_logger = logger("ERROR")

info_logger("Application started")
error_logger("Database connection failed")


print("\n==============================")
print("DECORATOR CONNECTION")
print("==============================\n")


# decorators internally use closures

def decorator(func):

    def wrapper():

        print("Before function")

        func()

        print("After function")

    return wrapper


def greet():

    print("Hello")


new_function = decorator(greet)

new_function()

# wrapper remembers func
# this is closure


print("\n==============================")
print("IMPORTANT NOTES")
print("==============================\n")


# first-class function:
#
# function behaves like normal object
#
#
# closure:
#
# inner function remembers outer variables
#
#
# nonlocal:
#
# allows modifying outer variable
#
#
# closures are heavily used in:
#
# decorators
# callbacks
# state management
# function factories


print("done")