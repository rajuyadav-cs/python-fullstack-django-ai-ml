class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount

    def current_balance(self):
        return self.balance