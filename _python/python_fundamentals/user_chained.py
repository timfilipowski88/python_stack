class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.user_balance = 0

    def display_user_balance(self):
        print(f"User: {self.name} -- Balance : ${self.user_balance}")

    def make_withdrawl(self, amount):
        self.user_balance -= amount
        return self

    def make_deposit(self, amount):
        self.user_balance += amount
        return self

    def tansfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)


john_doe = User('John Doe', 'jdoe@mail.com')
jane_doe = User('Jane Doe', 'janedoe@mail.com')
tim_fil = User('Tim Filipowski', 'timfilipowski88@gmail.com')

john_doe.make_deposit(80).make_deposit(90).make_deposit(100).make_withdrawl(20).display_user_balance()

jane_doe.make_deposit(125).make_deposit(225).make_withdrawl(80).make_withdrawl(20).display_user_balance()

tim_fil.make_deposit(400).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

john_doe.tansfer_money(tim_fil, 100)
john_doe.display_user_balance()
tim_fil.display_user_balance()