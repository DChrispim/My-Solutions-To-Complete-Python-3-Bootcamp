
class Account:
    
    def __init__(self, owner="John Doe", balance=0):
        """
        Initialize an Account object.

        :param owner: Owner of the account (default is "John Doe")
        :param balance: Initial balance of the account (default is 0)
        """
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        """
        Return a string representation of the Account object.
        """
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
        
    def deposit(self, amount):
        """
        Deposit funds into the account.

        :param amount: Amount to deposit
        """
        self.balance += amount
        print(f"Deposit Accepted! The new balance is {self.balance}")
        
    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        :param amount: Amount to withdraw
        """
        if amount > self.balance:
            raise ValueError("Funds Unavailable! The balance is insufficient to withdraw {}".format(amount))
        
        self.balance -= amount
        print(f"Withdrawal Accepted! The new balance is {self.balance}")
