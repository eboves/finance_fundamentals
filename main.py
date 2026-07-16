from account import Account
from transaction import Transaction

amex = Account("Amex", 800, "2026-07-16")
amex.deposit(250)
amex.deposit(300)
print(amex.transactions)
print(amex)