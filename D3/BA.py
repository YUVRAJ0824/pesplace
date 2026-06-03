class BankAccount:
    interest_rate = 0.05
    def __init__(self, balance):
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    @classmethod
    def set_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def get_valid_amount(amount):
        return amount > 0
#ats ressume to reach above 90 and remake resume 2copy hard/soft.
#Assignment-banking application mangement system using d3 topics
acc = BankAccount(1000)
acc.deposit(500)
BankAccount.set_rate(0.02)
print(BankAccount.get_valid_amount(-100))