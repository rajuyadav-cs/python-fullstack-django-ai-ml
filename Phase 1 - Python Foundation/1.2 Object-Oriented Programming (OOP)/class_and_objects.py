# Classes objects 

# __init__ are use to initiate a constructor in a class
# self is defined as the object which are using by the class
# attributes are like parameters of class

# creating a class

class Bank:

    # class attribute
    bank_name = "State Bank Of India"

# Constructor initialization
    def __init__(self,holder_name, balance, total_amount, interest):
        # constructor attribute
        self.holder_name = holder_name
        self.balance = balance
        self.total_amount = total_amount
        self.interest = interest
    
    # Method Creation
    def applyInterest(self):
        return self.balance + self.interest
    
    def total(self):
        return self.total_amount

#object creation
user1 = Bank('Ruuh',1000,10000,100)

#Accessing class attribute

print(Bank.bank_name)
print(f"Account Details:\n{user1.holder_name} {user1.balance} {user1.interest} {user1.total_amount}") 

# calling methods using object
print(user1.applyInterest())
print(user1.total())

# Changing objects attributes
user1.holder_name = "Ravi"
print(user1.holder_name)

#class attribute can be access by any object
user2 = Bank('Shiv',20000,200000,10000)

print(user1.bank_name)
print(user2.bank_name)

# __dict__ helps to show object all attributes

print(user1.__dict__)

# dir() helps to show all methods and attributes of object

print(dir(user1))

# Student Management System

class Student:

    school = "ABC School"

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def show(self):

        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


s1 = Student("Raju", 90)
s2 = Student("Aman", 85)

s1.show()
s2.show()

