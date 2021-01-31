class bank_account:
    def __init__(self, int_rate, balance=0):
        self.user_balance = balance
        self.account_yield = float(int_rate)

    def deposit(self, amount):
        self.user_balance += amount
        return self
    
    def withdrawl(self, amount):
        self.user_balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account has a balance of {self.user_balance} and an interest rate of {self.account_yield * 100}%")

    def yield_interest(self):
        if self.user_balance > 0:
            self.user_balance += self.user_balance * self.account_yield
            return self

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account = bank_account(int_rate=0.02, balance=0)

    def display_user_balance(self):
        print(f"User: {self.name} -- Balance : ${self.account.user_balance}")

    def make_withdrawl(self, amount):
        self.account.user_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account.user_balance += amount
        return self

    def tansfer_money(self, other_user, amount):
        self.account.withdrawl(amount)
        other_user.account.deposit(amount)

    def yield_interest(self):
        return self.account.yield_interest()

john_doe = User('John Doe', 'jdoe@mail.com')
jane_doe = User('Jane Doe', 'janedoe@mail.com')
tim_fil = User('Tim Filipowski', 'timfilipowski88@gmail.com')

# account_1 = bank_account("account_1",0.08, 100)
# account_2 = bank_account("account_2",0.06, 110)

john_doe.make_deposit(100).make_deposit(150).make_deposit(500).make_withdrawl(200).yield_interest().display_account_info()
tim_fil.make_deposit(150).make_deposit(200).make_withdrawl(80).make_withdrawl(20).make_withdrawl(50).make_withdrawl(150).yield_interest().display_account_info()

