# Decorators are use to add a layer to the another functions or like adding more features to it

def Decorator_func(func):
    def Wrapper_func():
        print("Before Wrapper func")
        func()
        print("After Wrapper func")

    return Wrapper_func

def greet():
    print("This is Wrapped function")

x = Decorator_func(greet)
x()

# @decorator method can also be use to make it more easier

def casefunc(func):
    def upperCase():
        return func().upper()
    
    return upperCase

@casefunc
def stringfunc():
    return "hello my friend"

print(stringfunc())


# Adding parameters or taking arguments in decorators
# using *args and **kwargs
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


# Decorators can accept their own arguments by adding another wrapper level.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())


'''
Multiple Decorators
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.
'''

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

'''
Preserving Function Metadata
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

Normally, a function's name can be returned with the __name__ attribute:
But, when a function is decorated, the metadata of the original function is lost.
To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.

'''

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)