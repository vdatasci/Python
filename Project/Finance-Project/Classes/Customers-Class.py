class Customer(object):
    members = []
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.members.append(str(name) + ', ' + str(balance) + ', ')
    
    def withdrawl(self, amount):
        if int(amount)>self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= int(amount)
        return self.balance
    
    def deposit(self, amount):
        self.balance += int(amount)
        return self.balance

class logger:
    def __init__(self):
            self.data = []
    def __getitem__(self, key):
            return self.data[key]
    def __call__(self, item):
            self.data.append(item)
    def clear(self):
        self.data = []
        


#jv = Customer('Josh Voss', 50)

#jv.name
#jv.balance
#jv.withdrawl(10.0)
#jv
#jv.balance
