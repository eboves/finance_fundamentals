from account import Account

class CreditCard(Account):
    def __init__(self, name, amount, date, credit_limit):
        super().__init__(name, amount, date)
        self.credit_limit = credit_limit

    def __str__(self):
        return f"{self.name}, Balance: ${self.amount}, Available Credit: ${self.credit_limit}"