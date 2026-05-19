from abc import ABC, abstractmethod


# abstract class
class Payment(ABC):

    # abstract method
    @abstractmethod
    def pay(self):

        pass


# child class
class UPI(Payment):

    def pay(self):

        print("UPI payment successful")


# child class
class Card(Payment):

    def pay(self):

        print("Card payment successful")


u = UPI()
u.pay()

c = Card()
c.pay()


print("\n------------------\n")


# multiple abstract methods
class Shape(ABC):

    @abstractmethod
    def area(self):

        pass

    @abstractmethod
    def perimeter(self):

        pass


class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width

    def perimeter(self):

        return 2 * (self.length + self.width)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())


print("\n------------------\n")


# employee example
class Employee(ABC):

    @abstractmethod
    def salary(self):

        pass


class Developer(Employee):

    def salary(self):

        print("Developer Salary = 50000")


class Manager(Employee):

    def salary(self):

        print("Manager Salary = 80000")


d = Developer()
m = Manager()

d.salary()
m.salary()


print("\n------------------\n")


# animal example
class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass


class Dog(Animal):

    def sound(self):

        print("Bark")


class Cat(Animal):

    def sound(self):

        print("Meow")


animals = [Dog(), Cat()]

for a in animals:

    a.sound()


print("\n------------------\n")


# trying to create object of abstract class
# this will give error

# p = Payment()


print("done")