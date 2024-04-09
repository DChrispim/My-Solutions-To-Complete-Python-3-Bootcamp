
import unittest
from Account_class import *

class TestAccountClass(unittest.TestCase):

    def test_deposit(self):
        # Test with default values
        account1 = Account()
        account1.deposit(100)
        self.assertEqual(account1.balance, 100)
        
        # Test with custom values
        account2 = Account(owner="Alice", balance=500)
        account2.deposit(200)
        self.assertEqual(account2.balance, 700) 

    def test_withdraw(self):
        # Test with custom values
        account1 = Account(owner="Bob", balance=1000)
        account1.withdraw(700)
        self.assertEqual(account1.balance, 300) 

    def test_insufficient_funds(self):
        account = Account(owner="Charlie", balance=200)
        with self.assertRaises(ValueError):
            account.withdraw(300)
    
    def test_operations(self):
        # 1. Instantiate the class
        account = Account('Jose',100)
        self.assertEqual(account.balance, 100)
        self.assertEqual(account.owner, 'Jose')
        account.deposit(50)
        self.assertEqual(account.balance, 150)
        account.withdraw(75)
        self.assertEqual(account.balance, 75)
        with self.assertRaises(ValueError):
            account.withdraw(500)

if __name__ == '__main__':
    unittest.main()
