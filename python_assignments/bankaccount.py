class BankAccount:
    def __init__ (self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance- 5
            print("Insufficent Funds! Charging $5 Fee")
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

ba1 = BankAccount(0,2030210)
ba2 = BankAccount(.012, 2103413)

ba1.deposit(1000).deposit(123123).deposit(213).withdraw(2321321321).yield_interest().display_account_info()
ba2.deposit(1000).deposit(123123).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()