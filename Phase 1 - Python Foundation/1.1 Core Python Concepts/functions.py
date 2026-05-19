# Why we need function

'''
Function is a way which helps to create a particular group of code for reusability..
for example:
instead of writing
print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")

We can create a function

def greeting():
    print("HELLO WORLD")

Now we can call this function as much time as we want 

greeting()
greeting()
greeting()
greeting()
greeting()
greeting()
greeting()

This will do the same thing but with more ease and reusability of lines code
'''

# Creating a function

def firstfunc():
    print("Hello, this is the first function we created!")

# Calling a function

firstfunc() # A function wont execute until it would be called.

# Arguments and parameters

def argupara(name, standard): # name and standard are know as parameters which are defined while function definition
    print(f"My name is :{name} and I am in {standard}th.")

argupara('Ruuh',12) # 'Ruuh' and 12 is called as arguments which pass during the function calling

# return statement
# return is use to give back some value and end the function
# for example:

def returnprac():
    sumnum = 0
    for i in range(1,11):
        sumnum += i

    return sumnum

print(returnprac())  # this will print the value of sumnum which is returned by the function

# return none = if we wont pass any value while returning by function 


def returnnone():
    print("Return None")
    return 

print(returnnone())

# multiple return values

def returnmultiple():
    x = 1
    y = 2

    return x+y , x-y

first, second = returnmultiple()
print( first, second)

# default Parameters

def defaultpara(name = "ruuh",standard = 12):
    print(f"My name is {name} and I am in {standard}th.")

defaultpara()
defaultpara('Cane', 11)


# *args = Arbitrary arguments (tuple) **kwargs = Arbitrary keywords arguments {dictionary}

# Suppose we didnt know the no. of arguments we use *args and **kwargs

def argkwargs(*nums,**dic):
    for i in nums:
        print(i,end=" ")
    for key , value in dic.items():
        print(f"\nKeys : {key}, Values: {value}")


argkwargs(1,2,3,4,5,name ="Ruuh", standard = 12)




