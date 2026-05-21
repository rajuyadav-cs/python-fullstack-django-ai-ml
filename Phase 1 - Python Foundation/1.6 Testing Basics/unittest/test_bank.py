import unittest
from bank import BankAccount


class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Starting all bank tests")

    @classmethod
    def tearDownClass(cls):
        print("Finished all bank tests")

    def setUp(self):
        self.account = BankAccount("Ruuh", 1000)

    def tearDown(self):
        print("Cleaning after test")

    def test_initial_balance(self):
        self.assertEqual(self.account.current_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.current_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.current_balance(), 800)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(5000)

    def test_owner_name(self):
        self.assertIsInstance(self.account.owner, str)

    def test_balance_greater_than_zero(self):
        self.assertGreater(self.account.current_balance(), 0)

    def test_subtests(self):
        cases = [
            (100, 1100),
            (200, 1200),
            (300, 1300),
        ]

        for amount, expected in cases:
            with self.subTest(amount=amount):
                account = BankAccount("Ruuh", 1000)
                account.deposit(amount)
                self.assertEqual(account.current_balance(), expected)

    @unittest.skip("Loan feature is not ready")
    def test_loan_feature(self):
        self.account.loan(1000)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(self.account.balance, 999999999)


if __name__ == "__main__":
    unittest.main(verbosity=2)