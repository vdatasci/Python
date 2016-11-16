class Customer(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def withdrawl(self, amount):
        if int(amount)>self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= int(amount)
        return self.balance
    
    def deposit(self, amount):
        self.balance += int(amount)
        return self.balance

    def transaction_history(self):
        


#jv = Customer('Josh Voss', 50)

#jv.name
#jv.balance
#jv.withdrawl(10.0)
#jv
#jv.balance


