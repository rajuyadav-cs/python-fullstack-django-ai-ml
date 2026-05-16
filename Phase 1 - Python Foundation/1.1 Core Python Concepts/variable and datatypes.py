'''Variable are like a container which are use to store some value.'''
name = "Raju" # text 
age = 21  # number
height = 5.8 # decimal number

# python Dynamically typed language, we can change the type of variable
name = 123
age = "Twenty One"

# Integer 
age = 21
marks = 95

# Float

price = 99.99
height = 5.8

#String

name = "Raju"
city = 'Delhi' 

# Boolean
is_student = True
is_employed = False

#String Slicing

print(name[0:3])

# Checking the Type of a Variable
print(type(name))
print(type(age ))
print(type(price))
print(type(height))
print(type(is_student))
print(type(is_employed))

# Type Conversion

print(float(age)) # converting integer to float
print(int(price)) # converting float to integer
print(str(age)) # converting integer to string


# OPERATORS

a = 10
b = 5
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# Comparison Operators
print(a > b) # Greater than
print(a < b) # Less than
print(a == b) # Equal to
print(a != b) # Not equal to
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

# Logical Operators
x = True
y = False
print(x and y) # Logical AND
print(x or y) # Logical OR
print(not x) # Logical NOT

# Assignment Operators
c = 10
c += 5 # c = c + 5
print(c)
c -= 3 # c = c - 3
print(c)
c *= 2 # c = c * 2
print(c)
c /= 4 # c = c / 4
print(c)
c %= 3 # c = c % 3
print(c)
c **= 2 # c = c ** 2
print(c)

# F-String
name = "Raju"
age = 21
print(f"My name is {name} and I am {age} years old.")

# Decimal Formatting
pi = 3.14159
print(f"Value of pi: {pi:.2f}") # Output: Value of pi: 3.14


# Task 1

name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Task 2

length = 10
width = 5
area = length * width
print(f"Area of rectangle with length {length} and width {width} is {area}.")

# Task 3

number = 7
if number % 2 == 0:
    print(f"{number} is an even number.")
else:    print(f"{number} is an odd number.")
