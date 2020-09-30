class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self.account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:${self.account_balance}")
    def  transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)

todd = User("Todd", "todd.smith@gmail.com")
sara = User("Sara","sara.smith@gmail.com")
jim = User("Jim", "jim.smith@gmail.com")

todd.make_deposit(100)
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

jim.transfer_money(todd, 5000)
jim.display_user_balance()
todd.display_user_balance()