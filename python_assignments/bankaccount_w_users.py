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

# ba1 = BankAccount(0,2030210)
# ba2 = BankAccount(.012, 2103413)

# ba1.deposit(1000).deposit(123123).deposit(213).withdraw(2321321321).yield_interest().display_account_info()
# ba2.deposit(1000).deposit(123123).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()
class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance = 0)
    def make_withdrawl(self, amount):
        self.account.withdraw = amount
        return self

    def make_deposit(self, amount):
        self.account.deposit = amount
        return self.account

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account.display_account_info}")

todd = User("Todd", "todd.smith@gmail.com")
sara = User("Sara","sara.smith@gmail.com")
jim = User("Jim", "jim.smith@gmail.com")

todd.account.deposit(100)
todd.make_deposit(100)
todd.make_deposit(100)
todd.make_withdrawl(300)
todd.display_user_balance()

sara.make_deposit(800)
sara.make_deposit(1500)
sara.make_withdrawl(200)
sara.make_withdrawl(234)
sara.display_user_balance()

jim.make_deposit(3000000)
jim.make_withdrawl(2500)
jim.make_withdrawl(13000)
jim.make_withdrawl(2400)
jim.display_user_balance()