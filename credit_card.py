from account import Account
from transaction import Transaction

class CreditCard(Account):
    def __init__(self, name, amount, date, credit_limit):
        super().__init__(name, amount, date)
        self.credit_limit = credit_limit

    def __str__(self):
        return f"{self.name}, Balance: ${self.amount}, Available Credit: ${self.credit_limit}"

    def withdraw(self, amount):
        #      -2500 - 3000 = -5500 > -(5000)
        if self.amount - amount < -self.credit_limit:
            return False
        else:
            self.amount = self.amount - amount
            today = self._get_today()
            transac = Transaction(amount, today, "withdraw")
            self.transactions.append(transac)
        return True
    
    def deposit(self, amount):

        if amount > abs(self.amount):
            return False
        else:
            self.amount = self.amount + amount
            today = self._get_today()
            transac = Transaction(amount, today, "deposit")
            self.transactions.append(transac)
        return True
        