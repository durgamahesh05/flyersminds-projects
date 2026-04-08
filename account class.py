class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

class SavingsAccount(Account):
    def __init__(self, owner, balance=0.0, interest_rate=0.02):
      
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")
my_savings = SavingsAccount("Jordan", 1000, 0.05)

my_savings.deposit(500)

my_savings.apply_interest()