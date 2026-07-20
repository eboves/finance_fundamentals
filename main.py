from account import Account
from credit_card import CreditCard
from transaction import Transaction

amex = Account("Amex", 800, "2026-07-16")
chase = CreditCard("Chase Sapphire", 0, "2026-07-18", 5000)


chase.deposit(500)
print(chase)


# user_type = int(input("Please type 1 for deposit and 2 for withdraw: "))

# if user_type == 1:
#     deposit_amount_input = float(input("Please enter an amount to deposit: "))
#     amex.deposit(deposit_amount_input)
# else:
#     withdraw_amount_input = float(input("Please enter an amount to withdraw: $ "))

#     while not amex.withdraw(withdraw_amount_input):
#         withdraw_amount_input = int(input("Please enter an amount to withdraw: $ "))
    
# print(amex.transactions)
# print(amex)