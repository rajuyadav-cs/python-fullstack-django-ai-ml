# test_pytest_examples.py

# pytest is a modern Python testing framework
# install:
# pip install pytest

import pytest


# ==========================================================
# SAMPLE CLASS FOR TESTING
# ==========================================================

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


# ==========================================================
# FIXTURE
# ==========================================================

# @pytest.fixture creates reusable setup
#
# fixture automatically runs when its name
# is passed inside a test function parameter

@pytest.fixture
def account():

    print("Creating fresh bank account")

    # this object will be passed into tests

    return BankAccount("Ruuh", 1000)


# ==========================================================
# SIMPLE ASSERTION TEST
# ==========================================================

# pytest uses normal Python assert

def test_initial_balance(account):

    # account fixture automatically executed
    # and injected here

    assert account.current_balance() == 1000


print("\n--------------------\n")


# ==========================================================
# TEST DEPOSIT
# ==========================================================

def test_deposit(account):

    account.deposit(500)

    assert account.current_balance() == 1500


print("\n--------------------\n")


# ==========================================================
# TEST WITHDRAW
# ==========================================================

def test_withdraw(account):

    account.withdraw(200)

    assert account.current_balance() == 800


print("\n--------------------\n")


# ==========================================================
# TEST EXCEPTION
# ==========================================================

# pytest.raises() checks whether
# expected exception is raised or not

def test_negative_deposit(account):

    with pytest.raises(ValueError):

        account.deposit(-100)


print("\n--------------------\n")


# ==========================================================
# TEST INSUFFICIENT BALANCE
# ==========================================================

def test_insufficient_balance(account):

    with pytest.raises(ValueError):

        account.withdraw(5000)


print("\n--------------------\n")


# ==========================================================
# TYPE CHECKING
# ==========================================================

def test_owner_type(account):

    assert isinstance(account.owner, str)


print("\n--------------------\n")


# ==========================================================
# GREATER THAN CHECK
# ==========================================================

def test_balance_positive(account):

    assert account.current_balance() > 0


print("\n--------------------\n")


# ==========================================================
# PARAMETRIZE
# ==========================================================

# parametrize runs same test multiple times
#
# first argument:
# parameter names
#
# second argument:
# list of test values

@pytest.mark.parametrize(
    "deposit_amount, expected",
    [
        (100, 1100),
        (200, 1200),
        (300, 1300),
    ]
)
def test_multiple_deposits(
    deposit_amount,
    expected
):

    account = BankAccount("Ruuh", 1000)

    account.deposit(deposit_amount)

    assert account.current_balance() == expected


print("\n--------------------\n")


# ==========================================================
# SKIP TEST
# ==========================================================

# this test will not run

@pytest.mark.skip(
    reason="Loan feature not ready"
)
def test_loan_feature():

    assert True


print("\n--------------------\n")


# ==========================================================
# EXPECTED FAILURE
# ==========================================================

# xfail means:
# we already know this test may fail

@pytest.mark.xfail
def test_expected_failure():

    assert 1 == 2


print("\n--------------------\n")


# ==========================================================
# FIXTURE WITH SETUP + CLEANUP
# ==========================================================

# code before yield -> setup
#
# code after yield -> cleanup

@pytest.fixture
def temp_data():

    print("Setup temp data")

    data = [1, 2, 3]

    yield data

    print("Cleanup temp data")


def test_temp_data(temp_data):

    assert len(temp_data) == 3


print("\n--------------------\n")


# ==========================================================
# FIXTURE SCOPE
# ==========================================================

# scope="module"
# fixture created once per file

@pytest.fixture(scope="module")
def shared_data():

    print("Creating shared data")

    return {"name": "Ruuh"}


def test_shared_1(shared_data):

    assert shared_data["name"] == "Ruuh"


def test_shared_2(shared_data):

    assert isinstance(shared_data, dict)


print("\n--------------------\n")


# ==========================================================
# SIMPLE BOOLEAN ASSERTIONS
# ==========================================================

def test_boolean():

    assert True


def test_false_condition():

    assert not False


print("\n--------------------\n")


# ==========================================================
# MEMBERSHIP ASSERTION
# ==========================================================

def test_membership():

    assert "a" in "apple"


print("\n--------------------\n")


# ==========================================================
# FLOAT ASSERTION
# ==========================================================

def test_float():

    result = 0.1 + 0.2

    # round used because float precision issue exists

    assert round(result, 1) == 0.3


print("\n--------------------\n")


# ==========================================================
# TEST DISCOVERY NOTES
# ==========================================================

# pytest automatically discovers:
#
# test_*.py
# *_test.py
#
# and functions starting with:
#
# test_


print("\n--------------------\n")


# ==========================================================
# IMPORTANT COMMANDS
# ==========================================================

# run all tests
#
# pytest
#
# verbose mode
#
# pytest -v
#
# run specific file
#
# pytest test_pytest_examples.py
#
# run specific function
#
# pytest test_pytest_examples.py::test_deposit


print("\n--------------------\n")


# ==========================================================
# INTERNAL FLOW OF PYTEST
# ==========================================================

# pytest:
#
# 1. discovers test files
# 2. discovers test functions
# 3. checks fixtures needed
# 4. executes fixtures first
# 5. injects fixture return values
# 6. runs assertions
# 7. shows report


print("done")