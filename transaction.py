class Transaction:
    def __init__(self, amount, date, type):
        self.amount = amount
        self.date = date
        self.type = type

    def __str__(self):
        return f"You had {self.type}: ${self.amount} on {self.date}"
    
    def __repr__(self):
        return f"Transaction({self.amount}, '{self.date}', '{self.type}')"