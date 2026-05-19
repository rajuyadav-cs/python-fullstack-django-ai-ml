# ==========================================================
# PYTHON INHERITANCE - COMPLETE GUIDE
# ==========================================================
#
# This file explains:
#
# 1. What is inheritance?
# 2. Parent and child classes
# 3. Single inheritance
# 4. Method overriding
# 5. super()
# 6. Multiple inheritance
# 7. Multi-level inheritance
# 8. Hierarchical inheritance
# 9. MRO (Method Resolution Order)
# 10. isinstance()
# 11. issubclass()
#
# ==========================================================


# ==========================================================
# WHAT IS INHERITANCE?
# ==========================================================
#
# Inheritance allows one class to use
# properties and methods of another class.
#
# Purpose:
#
# - Code reuse
# - Better structure
# - Less repetition
#
# ==========================================================


# ==========================================================
# 1. BASIC INHERITANCE
# ==========================================================
#
# Parent Class -> Animal
# Child Class  -> Dog
#
# Dog can use methods of Animal
#
# ==========================================================

print("\n--- Example 1: Basic Inheritance ---")


# Parent class
class Animal:

    def eat(self):

        print("Animal is eating")


# Child class inherits Animal
class Dog(Animal):

    def bark(self):

        print("Dog is barking")


# Create object
d = Dog()

# Child class method
d.bark()

# Parent class method inherited
d.eat()


# ==========================================================
# 2. SINGLE INHERITANCE
# ==========================================================
#
# One child class inherits one parent class
#
# ==========================================================

print("\n--- Example 2: Single Inheritance ---")


class Vehicle:

    def start(self):

        print("Vehicle started")


class Car(Vehicle):

    def drive(self):

        print("Car is driving")


c = Car()

c.start()
c.drive()


# ==========================================================
# 3. METHOD OVERRIDING
# ==========================================================
#
# Child class replaces parent method
#
# ==========================================================

print("\n--- Example 3: Method Overriding ---")


class Animal:

    def sound(self):

        print("Animal makes sound")


class Dog(Animal):

    # Overriding parent method
    def sound(self):

        print("Dog barks")


d = Dog()

d.sound()


# ==========================================================
# 4. super() FUNCTION
# ==========================================================
#
# super() is used to access parent class
#
# Mostly used to call parent constructor
#
# ==========================================================

print("\n--- Example 4: super() Function ---")


class Person:

    def __init__(self, name):

        self.name = name

        print("Person constructor called")


class Student(Person):

    def __init__(self, name, marks):

        # Calling parent constructor
        super().__init__(name)

        self.marks = marks

        print("Student constructor called")


s = Student("Raju", 95)

print(s.name)
print(s.marks)


# ==========================================================
# 5. WHY super() IS IMPORTANT
# ==========================================================
#
# Without super():
#
# Parent constructor will not execute
#
# ==========================================================

print("\n--- Example 5: Without super() ---")


class Parent:

    def __init__(self):

        print("Parent constructor")


class Child(Parent):

    def __init__(self):

        print("Child constructor")


c = Child()

# Parent constructor NOT called


# ==========================================================
# 6. MULTIPLE INHERITANCE
# ==========================================================
#
# One child inherits multiple parents
#
# ==========================================================

print("\n--- Example 6: Multiple Inheritance ---")


class Father:

    def skills(self):

        print("Driving")


class Mother:

    def talent(self):

        print("Cooking")


class Child(Father, Mother):

    def hobby(self):

        print("Gaming")


c = Child()

c.skills()
c.talent()
c.hobby()


# ==========================================================
# 7. MULTI-LEVEL INHERITANCE
# ==========================================================
#
# Grandparent -> Parent -> Child
#
# ==========================================================

print("\n--- Example 7: Multi-Level Inheritance ---")


class Animal:

    def eat(self):

        print("Eating")


class Mammal(Animal):

    def walk(self):

        print("Walking")


class Dog(Mammal):

    def bark(self):

        print("Barking")


d = Dog()

d.eat()
d.walk()
d.bark()


# ==========================================================
# 8. HIERARCHICAL INHERITANCE
# ==========================================================
#
# One parent -> Multiple children
#
# ==========================================================

print("\n--- Example 8: Hierarchical Inheritance ---")


class Animal:

    def eat(self):

        print("Animal eating")


class Dog(Animal):

    def bark(self):

        print("Dog barking")


class Cat(Animal):

    def meow(self):

        print("Cat meowing")


d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()


# ==========================================================
# 9. METHOD RESOLUTION ORDER (MRO)
# ==========================================================
#
# Python searches methods left to right
#
# ==========================================================

print("\n--- Example 9: MRO ---")


class A:

    def show(self):

        print("Class A")


class B:

    def show(self):

        print("Class B")


class C(A, B):

    pass


obj = C()

# A comes first
obj.show()

# Display method resolution order
print(C.mro())


# ==========================================================
# 10. isinstance()
# ==========================================================
#
# Checks object belongs to class or not
#
# ==========================================================

print("\n--- Example 10: isinstance() ---")


class Animal:
    pass


class Dog(Animal):
    pass


d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))


# ==========================================================
# 11. issubclass()
# ==========================================================
#
# Checks inheritance relationship
#
# ==========================================================

print("\n--- Example 11: issubclass() ---")

print(issubclass(Dog, Animal))


# ==========================================================
# 12. REAL PROJECT EXAMPLE
# ==========================================================
#
# Employee Management System
#
# ==========================================================

print("\n--- Example 12: Real Project Example ---")


# Parent class
class Employee:

    def __init__(self, name):

        self.name = name

    def show_name(self):

        print(f"Employee Name: {self.name}")


# Child class
class Developer(Employee):

    def __init__(self, name, language):

        # Parent constructor
        super().__init__(name)

        self.language = language

    def show_language(self):

        print(f"Programming Language: {self.language}")


# Create object
dev = Developer("Raju", "Python")

dev.show_name()
dev.show_language()


# ==========================================================
# 13. ATTRIBUTE INHERITANCE
# ==========================================================
#
# Child inherits parent attributes too
#
# ==========================================================

print("\n--- Example 13: Attribute Inheritance ---")


class Person:

    def __init__(self):

        self.country = "India"


class Student(Person):

    pass


s = Student()

print(s.country)


# ==========================================================
# 14. ACCESSING PARENT METHOD DIRECTLY
# ==========================================================

print("\n--- Example 14: Parent Method Access ---")


class Parent:

    def display(self):

        print("Parent display")


class Child(Parent):

    def display(self):

        # Call parent method
        super().display()

        print("Child display")


c = Child()

c.display()


# ==========================================================
# IMPORTANT INTERVIEW QUESTIONS
# ==========================================================
#
# Q1. Why use inheritance?
#
# - Reusability
# - Better code organization
# - Less repetition
#
#
# Q2. What is method overriding?
#
# Child class replacing parent method
#
#
# Q3. What does super() do?
#
# Accesses parent class methods/constructor
#
#
# Q4. What is MRO?
#
# Method Resolution Order
#
# Python checks classes from left to right
#
# ==========================================================


# ==========================================================
# BEST PRACTICES
# ==========================================================
#
# 1. Use inheritance only for "IS-A" relationship
#
# GOOD:
# Dog is an Animal
#
# BAD:
# Car is a Driver
#
#
# 2. Use super() properly
#
#
# 3. Avoid unnecessary deep inheritance
#
#
# 4. Keep parent classes generic
#
# ==========================================================


# ==========================================================
# FINAL SUMMARY
# ==========================================================
#
# Inheritance:
#     Reusing code from another class
#
# Parent Class:
#     Base class
#
# Child Class:
#     Derived class
#
# super():
#     Access parent class
#
# Overriding:
#     Replacing parent method
#
# Multiple Inheritance:
#     One child, multiple parents
#
# MRO:
#     Method search order
#
# ==========================================================


# ==========================================================
# END OF FILE
# ==========================================================