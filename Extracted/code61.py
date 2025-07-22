# Code #61: Create a Class for Bank Account with Deposit & Without
"""
    🧠 Why This Matters?
    Used in:
    - ✍️ Finance and ledger systems
    - 🔒 Data encapsulation (private balance)
    - 💳 Interactive banking simulations
    - 🧱 Real-world object modeling (OOP at its core
"""
# Tier: Intermediate
# Goal: Build a class that handles deposit, withdrawal, and balance display securely

class BankAccount:
    def __init__ (self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance
    
# Sample Usage

account = BankAccount("Sena", 5000)
account.deposit(1500)
account.withdraw(2000)
print("Final balance:", account.get_balance())

# Sample Output
"""
    Deposited ₹1500. New Balance: ₹6500
    Withdrew ₹2000. New Balance: ₹4500
    Final Balance: 4500
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    __int__         Constructor initialize account owner & balance
    __balance       Encapsulation via private variable
    deposit()       Adds amount with validation
    withdraw()      Deducts amount with safety check
    get_balance()   Controlled read access to private balance
"""
# This class can be extended with interest, overdraft, multi-account features, or transaction logs.

# Real-World Connection
"""
    - Online banking modules
    - FinTech backend engines
    - Personal finance management tools
    - ATM or mobile wallet simulations
"""
        