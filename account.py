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
        self.amount = amount + self.amount   
        today = datetime.today().strftime('%Y-%m-%d')
        transac = Transaction(amount, today, 'deposit')
        self.transactions.append(transac)
