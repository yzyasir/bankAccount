class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.intrate = int_rate
        self.accbalance = balance
        self.personname = name

    def deposit(self, amount):
        self.accbalance += amount
        return self

    def withdraw(self, amount):
        self.accbalance -= amount
        return self

    def display_account_info(self):
        print(f"{self.personname} has ${self.accbalance} with {self.intrate} interest rate")
        return self

    def yield_interest(self):
        self.accbalance += self.intrate * self.accbalance
        return self


BankAccount1 = BankAccount("Yasir Zafar", 0.06, 100)
# BankAccount1 is an instance (applied the blueprint into bankaccount1)
BankAccount2 = BankAccount("Zaeema Zafar", 0.06, 1000)
# Note how im targeting the class then a number, and then the attribute after the dot

BankAccount1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest()

BankAccount2.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest()
# All I did above was the arithmatic for the methods I made in the class of BankAccount


BankAccount1.display_account_info()
BankAccount2.display_account_info()