'''
    Create Account class with 2 attributes - balance & account number
    Create methods for debit, credit & printing the balance
'''

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs.{amount} was debited")
        print(f"Total balance = {self.get_balance()}")

    # credit method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} was credited")
        print(f"Total balance = {self.get_balance()}")
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_number)

acc1.debit(500)
acc1.credit(50000)