# ==========================================================
# PYTHON CLASS METHODS & STATIC METHODS - COMPLETE GUIDE
# ==========================================================
#
# This file explains:
#
# 1. Instance Methods
# 2. Class Methods (@classmethod)
# 3. Static Methods (@staticmethod)
# 4. Difference between all methods
# 5. Alternative constructors
# 6. Real-world examples
#
# ==========================================================


# ==========================================================
# 1. INSTANCE METHODS
# ==========================================================
#
# Instance methods work with object data
#
# First parameter:
#     self
#
# self = current object
#
# ==========================================================

print("\n--- Example 1: Instance Method ---")


class Student:

    def __init__(self, name, age):

        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def show_details(self):

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Create object
s1 = Student("Raju", 21)

# Call instance method
s1.show_details()


# ==========================================================
# WHY INSTANCE METHODS?
# ==========================================================
#
# Used when method needs object-specific data
#
# Example:
#     self.name
#     self.age
#
# ==========================================================


# ==========================================================
# 2. CLASS METHODS
# ==========================================================
#
# Class methods work with class-level data
#
# Decorator:
#     @classmethod
#
# First parameter:
#     cls
#
# cls = current class
#
# ==========================================================

print("\n--- Example 2: Class Method ---")


class Employee:

    # Class attribute
    company = "Google"

    def __init__(self, name):

        self.name = name

    # Class method
    @classmethod
    def show_company(cls):

        print(f"Company: {cls.company}")


# Call class method
Employee.show_company()


# ==========================================================
# IMPORTANT:
#
# Class methods can access:
#     Class attributes
#
# Class methods should NOT directly use:
#     Instance attributes
#
# ==========================================================


# ==========================================================
# 3. MODIFYING CLASS VARIABLES
# ==========================================================
#
# Real use-case of class methods
#
# ==========================================================

print("\n--- Example 3: Modify Class Variable ---")


class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):

        cls.school = new_school


print("Before Change:", Student.school)

# Change class variable
Student.change_school("XYZ School")

print("After Change:", Student.school)


# ==========================================================
# 4. CLASS METHOD AS ALTERNATIVE CONSTRUCTOR
# ==========================================================
#
# Very common real-world use-case
#
# Used to create objects differently
#
# ==========================================================

print("\n--- Example 4: Alternative Constructor ---")


class User:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    # Alternative constructor
    @classmethod
    def from_string(cls, data):

        # Split string
        name, age = data.split("-")

        # Create and return object
        return cls(name, int(age))


# Create object using class method
u1 = User.from_string("Raju-21")

print(u1.name)
print(u1.age)


# ==========================================================
# WHY THIS IS USEFUL?
# ==========================================================
#
# Data often comes from:
#
# - Files
# - APIs
# - Databases
#
# Example:
#
# "Raju-21"
#
# Class methods help convert data into objects
#
# ==========================================================


# ==========================================================
# 5. STATIC METHODS
# ==========================================================
#
# Static methods do NOT use:
#
# - self
# - cls
#
# Used for utility/helper functions
#
# Decorator:
#     @staticmethod
#
# ==========================================================

print("\n--- Example 5: Static Method ---")


class Math:

    @staticmethod
    def add(a, b):

        return a + b


# Call static method
print(Math.add(10, 20))


# ==========================================================
# IMPORTANT:
#
# Static methods:
#
# - Do not access object data
# - Do not access class data
#
# They are independent utility methods
#
# ==========================================================


# ==========================================================
# 6. REAL-WORLD STATIC METHOD EXAMPLE
# ==========================================================

print("\n--- Example 6: Temperature Converter ---")


class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        return (celsius * 9/5) + 32


result = Temperature.celsius_to_fahrenheit(30)

print(result)


# ==========================================================
# 7. DIFFERENCE BETWEEN ALL METHODS
# ==========================================================

print("\n--- Example 7: All Methods Together ---")


class Demo:

    # Class attribute
    company = "OpenAI"

    def __init__(self, name):

        # Instance attribute
        self.name = name

    # Instance method
    def instance_method(self):

        print(f"Instance Method -> {self.name}")

    # Class method
    @classmethod
    def class_method(cls):

        print(f"Class Method -> {cls.company}")

    # Static method
    @staticmethod
    def static_method():

        print("Static Method -> Utility Function")


d = Demo("Raju")

d.instance_method()

Demo.class_method()

Demo.static_method()


# ==========================================================
# INTERNAL WORKING
# ==========================================================
#
# Instance Method:
#
# obj.method()
#
# internally:
#
# Class.method(obj)
#
#
# Class Method:
#
# Class.method()
#
# internally:
#
# Class.method(Class)
#
#
# Static Method:
#
# Nothing automatically passed
#
# ==========================================================


# ==========================================================
# 8. ACCESSING CLASS METHODS THROUGH OBJECT
# ==========================================================
#
# Possible but not preferred
#
# ==========================================================

print("\n--- Example 8: Access Through Object ---")


class Test:

    company = "Google"

    @classmethod
    def show_company(cls):

        print(cls.company)


t = Test()

# Works
t.show_company()


# ==========================================================
# 9. REAL PROJECT EXAMPLE
# ==========================================================
#
# Employee Management System
#
# ==========================================================

print("\n--- Example 9: Real Project Example ---")


class Employee:

    # Class attribute
    company = "Microsoft"

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    # Instance method
    def show_employee(self):

        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

    # Class method
    @classmethod
    def change_company(cls, new_company):

        cls.company = new_company

    # Static method
    @staticmethod
    def company_policy():

        print("Employees must follow company rules")


# Create object
e1 = Employee("Raju", 50000)

# Instance method
e1.show_employee()

# Class method
Employee.change_company("Google")

print(Employee.company)

# Static method
Employee.company_policy()


# ==========================================================
# 10. COMMON BEGINNER MISTAKES
# ==========================================================

print("\n--- Example 10: Common Mistakes ---")


class Example:

    company = "ABC"

    @staticmethod
    def wrong_method():

        # ERROR:
        # Cannot directly access class variables
        # without class name or cls

        print(Example.company)


Example.wrong_method()


# ==========================================================
# IMPORTANT INTERVIEW QUESTIONS
# ==========================================================
#
# Q1. Difference between instance method
#     and class method?
#
# Instance Method:
#     Works with object data
#
# Class Method:
#     Works with class data
#
#
# Q2. Difference between classmethod
#     and staticmethod?
#
# classmethod:
#     Uses cls
#
# staticmethod:
#     No cls, no self
#
#
# Q3. Why use static methods?
#
# Utility/helper functions
#
#
# Q4. Why use class methods?
#
# Class-level operations
#
# ==========================================================


# ==========================================================
# BEST PRACTICES
# ==========================================================
#
# 1. Use instance methods for object data
#
#
# 2. Use class methods for class-level changes
#
#
# 3. Use static methods for helper utilities
#
#
# 4. Do not overuse static methods
#
# ==========================================================


# ==========================================================
# FINAL SUMMARY
# ==========================================================
#
# Instance Method:
#     Uses self
#     Works with object data
#
#
# Class Method:
#     Uses cls
#     Works with class data
#
#
# Static Method:
#     Uses neither self nor cls
#     Utility/helper function
#
# ==========================================================


# ==========================================================
# END OF FILE
# ==========================================================