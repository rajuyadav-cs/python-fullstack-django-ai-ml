# dataclass_complete_guide.py

# dataclass helps reduce repetitive code
# specially for classes that mostly store data


from dataclasses import dataclass
from dataclasses import field


print("\n==============================")
print("BASIC DATACLASS")
print("==============================\n")


# without dataclass we normally write:
#
# class Student:
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#
# dataclass automatically creates __init__
# so we don't need to write it manually


@dataclass
class Student:

    # type hints
    name: str
    age: int
    marks: int


# object creation works automatically
s1 = Student("Raju", 21, 90)

print(s1)

# internally dataclass created:
#
# __init__
# __repr__
# __eq__


print("\n==============================")
print("AUTO GENERATED __init__")
print("==============================\n")


# we can directly access values
print(s1.name)
print(s1.age)
print(s1.marks)


print("\n==============================")
print("AUTO GENERATED __repr__")
print("==============================\n")


# print object nicely
print(s1)

# without dataclass output would look ugly
# like:
#
# <__main__.Student object at 0x0000>


print("\n==============================")
print("AUTO GENERATED __eq__")
print("==============================\n")


s2 = Student("Raju", 21, 90)

# compares data automatically
print(s1 == s2)

# without dataclass:
# objects compare by memory location


print("\n==============================")
print("DEFAULT VALUES")
print("==============================\n")


@dataclass
class Employee:

    name: str

    # default value
    salary: int = 25000

    department: str = "IT"


e1 = Employee("Aman")

print(e1)

# default values automatically used


print("\n==============================")
print("CUSTOM DEFAULT USING field()")
print("==============================\n")


# problem:
#
# mutable default values like list
# should not be used directly


# wrong way:
#
# items: list = []


# correct way:
#
# field(default_factory=list)


@dataclass
class Cart:

    items: list = field(default_factory=list)


c1 = Cart()
c2 = Cart()

c1.items.append("Laptop")

print(c1.items)
print(c2.items)

# both objects have separate lists


print("\n==============================")
print("__post_init__")
print("==============================\n")


# __post_init__ runs automatically
# after dataclass constructor finishes


@dataclass
class Product:

    name: str
    price: int

    def __post_init__(self):

        print("object created")

        # validation example
        if self.price < 0:

            raise ValueError(
                "price cannot be negative"
            )


p1 = Product("Phone", 50000)

print(p1)


print("\n==============================")
print("VALIDATION EXAMPLE")
print("==============================\n")


try:

    p2 = Product("Laptop", -1000)

except ValueError as e:

    print(e)


print("\n==============================")
print("FROZEN DATACLASS")
print("==============================\n")


# frozen=True makes object immutable
# values cannot be changed


@dataclass(frozen=True)
class Point:

    x: int
    y: int


p = Point(10, 20)

print(p)

# this will give error
#
# p.x = 100


print("\n==============================")
print("DATACLASS WITH METHODS")
print("==============================\n")


@dataclass
class Rectangle:

    length: int
    width: int

    # normal methods still work
    def area(self):

        return self.length * self.width


r = Rectangle(10, 5)

print(r)

print("Area:", r.area())


print("\n==============================")
print("DATACLASS INHERITANCE")
print("==============================\n")


@dataclass
class Person:

    name: str
    age: int


# child class inherits parent dataclass
@dataclass
class Student2(Person):

    marks: int


s = Student2("Raju", 21, 95)

print(s)

print(s.name)
print(s.age)
print(s.marks)


print("\n==============================")
print("field(init=False)")
print("==============================\n")


# init=False means:
# value will not be passed during object creation


@dataclass
class User:

    name: str

    id: int = field(init=False)

    def __post_init__(self):

        # generate id automatically
        self.id = 1001


u = User("Vikram")

print(u)


print("\n==============================")
print("REAL PROJECT STYLE EXAMPLE")
print("==============================\n")


@dataclass
class BankAccount:

    account_holder: str
    balance: int
    account_type: str = "Saving"

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:

            print("insufficient balance")

        else:

            self.balance -= amount


acc = BankAccount("Raju", 10000)

print(acc)

acc.deposit(5000)

print(acc)

acc.withdraw(3000)

print(acc)

acc.withdraw(50000)


print("\n==============================")
print("WHY DATACLASS IS USEFUL")
print("==============================\n")


# benefits:
#
# less boilerplate code
# automatic constructor
# automatic comparison
# automatic object printing
# cleaner classes
# better readability


print("dataclass reduces repetitive code")


print("\n==============================")
print("INTERNAL MAGIC")
print("==============================\n")


# this:
#
# @dataclass
# class Demo:
#     name: str
#
#
# internally becomes something similar to:
#
#
# class Demo:
#
#     def __init__(self, name):
#
#         self.name = name
#
#
#     def __repr__(self):
#
#         ...
#
#
#     def __eq__(self):
#
#         ...


print("python auto-generates methods")


print("\n==============================")
print("DONE")
print("==============================\n")