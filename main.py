class Account:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date
        self.transactions = []
    
    def __str__(self):
        return f"{self.name}, Balance: ${self.amount}"

amex = Account("Amex", 3245.45, "2026-07-14")
print(amex)