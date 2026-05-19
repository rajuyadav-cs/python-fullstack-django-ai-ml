'''
1. Local Scope
A variable created inside a function belongs to the local scope of that function. It only exists while the function is running and cannot be accessed from the outside.

'''
def my_func():
    x = "I am local"  # Local variable
    print(x)

my_func()  # Outputs: I am local
# print(x) # NameError: name 'x' is not defined

'''
2. Global Scope
A variable created in the main body of the Python script is in the global scope. It can be read from anywhere in the file, including inside functions.

'''
y = "I am global"  # Global variable

def read_global():
    print(y)  # Works perfectly!

read_global()  # Outputs: I am global

'''
3. Nonlocal Scope (Enclosing)
This applies to nested functions (a function inside a function). The nonlocal scope is the scope of the outer (enclosing) function.

If the inner function wants to modify a variable in the outer function, it must use the nonlocal keyword.

'''
def outer_func():
    message = "Hello from outer"  # Enclosing/Nonlocal variable
    
    def inner_func():
        nonlocal message  # Targets the variable in the outer function
        message = "Hi from inner!"
        
    inner_func()
    print(message)

outer_func()  # Outputs: Hi from inner!
