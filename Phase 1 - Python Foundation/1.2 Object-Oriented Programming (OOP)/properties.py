# properties_getter_setter.py


# normal class without property
class Student:

    def __init__(self, marks):

        self.marks = marks


s1 = Student(90)

print(s1.marks)

# problem:
# anyone can set invalid value

s1.marks = -100

print(s1.marks)


print("\n----------------------\n")


# using getter and setter manually
class Student2:

    def __init__(self, marks):

        self._marks = marks

    # getter
    def get_marks(self):

        return self._marks

    # setter
    def set_marks(self, value):

        if value < 0:

            print("marks cannot be negative")

        else:

            self._marks = value


s2 = Student2(80)

print(s2.get_marks())

s2.set_marks(95)

print(s2.get_marks())

s2.set_marks(-10)


print("\n----------------------\n")


# now using @property
class Student3:

    def __init__(self, marks):

        self._marks = marks

    @property
    def marks(self):

        return self._marks


s3 = Student3(70)

# looks like normal attribute
# but internally getter method runs
print(s3.marks)


print("\n----------------------\n")


# property with setter
class Student4:

    def __init__(self, marks):

        self._marks = marks

    # getter
    @property
    def marks(self):

        return self._marks

    # setter
    @marks.setter
    def marks(self, value):

        if value < 0:

            print("invalid marks")

        else:

            self._marks = value


s4 = Student4(88)

print(s4.marks)

# setter runs internally
s4.marks = 99

print(s4.marks)

s4.marks = -5


print("\n----------------------\n")


# read only property
class Circle:

    def __init__(self, radius):

        self.radius = radius

    @property
    def area(self):

        return 3.14 * self.radius * self.radius


c1 = Circle(5)

print(c1.area)

# this will give error because no setter
# c1.area = 100


print("\n----------------------\n")


# property with deleter
class Demo:

    def __init__(self, value):

        self._value = value

    @property
    def value(self):

        return self._value

    @value.deleter
    def value(self):

        print("deleting value")

        del self._value


d1 = Demo(50)

print(d1.value)

del d1.value


print("\n----------------------\n")


# practical example
class BankAccount:

    def __init__(self, balance):

        self._balance = balance

    @property
    def balance(self):

        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount < 0:

            print("balance cannot be negative")

        else:

            self._balance = amount


acc = BankAccount(1000)

print(acc.balance)

acc.balance = 2000

print(acc.balance)

acc.balance = -500


print("\n----------------------\n")


# another example
class Temperature:

    def __init__(self, temp):

        self._temp = temp

    @property
    def temp(self):

        return self._temp

    @temp.setter
    def temp(self, value):

        if value < -273:

            print("temperature below absolute zero not possible")

        else:

            self._temp = value


t = Temperature(25)

print(t.temp)

t.temp = 100

print(t.temp)

t.temp = -500


print("\n----------------------\n")


# internally what happens

# obj.data
# actually calls getter

# obj.data = value
# actually calls setter


print("done")