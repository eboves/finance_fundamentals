from datetime import datetime
from transaction import Transaction


class Account:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date
        self.transactions = []
    
    def __str__(self):
        return f"{self.name}, Balance: ${self.amount}"

    def deposit(self, amount):
        self.amount = self.amount + amount  
        today = self._get_today()
        transac = Transaction(amount, today, 'deposit')
        self.transactions.append(transac)

    def withdraw(self, amount):

        if amount > self.amount:
            return False
        else:
            self.amount = self.amount - amount
            today = self._get_today()
            transac = Transaction(amount, today, "withdraw")
            self.transactions.append(transac)

        return True

    def _get_today(self):
        return datetime.today().strftime('%Y-%m-%d')