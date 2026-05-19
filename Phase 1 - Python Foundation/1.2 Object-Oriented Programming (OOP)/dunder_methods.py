# ==========================================================
# PYTHON DUNDER / MAGIC METHODS - COMPLETE GUIDE
# ==========================================================
#
# This file explains:
#
# 1. What are magic methods?
# 2. __init__
# 3. __str__
# 4. __repr__
# 5. __len__
# 6. __eq__
# 7. Operator overloading basics
# 8. Real project examples
#
# ==========================================================


# ==========================================================
# WHAT ARE DUNDER / MAGIC METHODS?
# ==========================================================
#
# Dunder = Double Underscore
#
# Examples:
#
# __init__
# __str__
# __len__
# __eq__
#
# Python internally calls these methods automatically.
#
# They define object behavior.
#
# Example:
#
# len(obj)
#
# internally becomes:
#
# obj.__len__()
#
# ==========================================================


# ==========================================================
# 1. __init__ METHOD
# ==========================================================
#
# Constructor
#
# Automatically runs when object is created
#
# Used for initialization
#
# ==========================================================

print("\n--- Example 1: __init__ ---")


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

        print("Constructor called")


# Object creation
s1 = Student("Raju", 21)

print(s1.name)
print(s1.age)


# ==========================================================
# 2. __str__ METHOD
# ==========================================================
#
# Defines human-readable string representation
#
# Used by:
#
# print(object)
#
# ==========================================================

print("\n--- Example 2: __str__ ---")


class Employee:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Employee Name: {self.name}"


e1 = Employee("Aman")

# Automatically calls __str__()
print(e1)


# ==========================================================
# WHAT HAPPENS WITHOUT __str__ ?
# ==========================================================

print("\n--- Example 3: Without __str__ ---")


class Test:
    pass


t = Test()

# Ugly default output
print(t)


# ==========================================================
# 3. __repr__ METHOD
# ==========================================================
#
# Developer-friendly representation
#
# Mostly used for debugging
#
# repr(object)
#
# ==========================================================

print("\n--- Example 4: __repr__ ---")


class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def __repr__(self):

        return (
            f"Product(name='{self.name}', "
            f"price={self.price})"
        )


p1 = Product("Laptop", 50000)

# Calls __repr__
print(repr(p1))


# ==========================================================
# DIFFERENCE BETWEEN __str__ AND __repr__
# ==========================================================
#
# __str__:
#     User-friendly output
#
# __repr__:
#     Developer/debugging output
#
# If __str__ is missing,
# Python may use __repr__
#
# ==========================================================


# ==========================================================
# EXAMPLE USING BOTH __str__ AND __repr__
# ==========================================================

print("\n--- Example 5: __str__ vs __repr__ ---")


class Book:

    def __init__(self, title):

        self.title = title

    # User-friendly
    def __str__(self):

        return f"Book: {self.title}"

    # Developer-friendly
    def __repr__(self):

        return f"Book(title='{self.title}')"


b1 = Book("Python Basics")

print(str(b1))
print(repr(b1))


# ==========================================================
# 4. __len__ METHOD
# ==========================================================
#
# Defines behavior of len(object)
#
# ==========================================================

print("\n--- Example 6: __len__ ---")


class Team:

    def __init__(self, members):

        self.members = members

    def __len__(self):

        return len(self.members)


team = Team(["Raju", "Aman", "Vikram"])

# Calls __len__()
print(len(team))


# ==========================================================
# WITHOUT __len__
# ==========================================================

print("\n--- Example 7: Without __len__ ---")


class Demo:
    pass


d = Demo()

# Uncomment to see error
# print(len(d))

print("len() would fail without __len__")


# ==========================================================
# 5. __eq__ METHOD
# ==========================================================
#
# Defines behavior of == operator
#
# ==========================================================

print("\n--- Example 8: __eq__ ---")


class Person:

    def __init__(self, age):

        self.age = age

    def __eq__(self, other):

        return self.age == other.age


p1 = Person(21)
p2 = Person(21)

# Calls __eq__()
print(p1 == p2)


# ==========================================================
# WITHOUT __eq__
# ==========================================================
#
# Python compares memory addresses
#
# ==========================================================

print("\n--- Example 9: Without __eq__ ---")


class Student:

    def __init__(self, marks):

        self.marks = marks


s1 = Student(90)
s2 = Student(90)

# Different memory locations
print(s1 == s2)


# ==========================================================
# 6. OPERATOR OVERLOADING
# ==========================================================
#
# Magic methods allow operator overloading
#
# Example:
#
# +  -> __add__
# == -> __eq__
#
# ==========================================================

print("\n--- Example 10: Operator Overloading ---")


class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

# Calls __add__()
print(n1 + n2)


# ==========================================================
# 7. __lt__ METHOD
# ==========================================================
#
# Less than operator <
#
# ==========================================================

print("\n--- Example 11: __lt__ ---")


class Marks:

    def __init__(self, score):

        self.score = score

    def __lt__(self, other):

        return self.score < other.score


m1 = Marks(80)
m2 = Marks(90)

print(m1 < m2)


# ==========================================================
# COMMON MAGIC METHODS
# ==========================================================
#
# __init__   -> Constructor
# __str__    -> print()
# __repr__   -> repr()
# __len__    -> len()
# __eq__     -> ==
# __add__    -> +
# __sub__    -> -
# __mul__    -> *
# __lt__     -> <
# __gt__     -> >
#
# ==========================================================


# ==========================================================
# 8. REAL PROJECT EXAMPLE
# ==========================================================
#
# Shopping Cart System
#
# ==========================================================

print("\n--- Example 12: Real Project Example ---")


class Cart:

    def __init__(self, items):

        self.items = items

    # String representation
    def __str__(self):

        return f"Cart with {len(self.items)} items"

    # Length behavior
    def __len__(self):

        return len(self.items)

    # Equality comparison
    def __eq__(self, other):

        return len(self.items) == len(other.items)


cart1 = Cart(["Laptop", "Mouse"])
cart2 = Cart(["Phone", "Watch"])

print(cart1)

print(len(cart1))

print(cart1 == cart2)


# ==========================================================
# INTERNAL WORKING
# ==========================================================
#
# print(obj)
# -> obj.__str__()
#
#
# len(obj)
# -> obj.__len__()
#
#
# obj1 == obj2
# -> obj1.__eq__(obj2)
#
#
# obj1 + obj2
# -> obj1.__add__(obj2)
#
# ==========================================================


# ==========================================================
# IMPORTANT INTERVIEW QUESTIONS
# ==========================================================
#
# Q1. What are magic methods?
#
# Special methods automatically called by Python
#
#
# Q2. Difference between __str__ and __repr__?
#
# __str__:
#     User-friendly
#
# __repr__:
#     Developer/debugging
#
#
# Q3. Why use __eq__?
#
# To customize == comparison
#
#
# Q4. Why use __len__?
#
# To support len(object)
#
# ==========================================================


# ==========================================================
# BEST PRACTICES
# ==========================================================
#
# 1. Use __str__ for clean output
#
#
# 2. Use __repr__ for debugging
#
#
# 3. Keep magic methods simple
#
#
# 4. Use operator overloading carefully
#
# ==========================================================


# ==========================================================
# FINAL SUMMARY
# ==========================================================
#
# __init__:
#     Object initialization
#
# __str__:
#     Human-readable object output
#
# __repr__:
#     Developer/debugging representation
#
# __len__:
#     Defines len(object)
#
# __eq__:
#     Defines == behavior
#
# Magic methods:
#     Customize object behavior in Python
#
# ==========================================================


# ==========================================================
# END OF FILE
# ==========================================================