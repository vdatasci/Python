class stock:
    creatorsname = 'Josh Voss'
    def __init__(self, name, price):
            self.name = name
            self.price = price
    def __getitem__(self, i):
        return self.name[i]
    def __iter__(self):
        return self.name.itervalues()

x = stock('VOS', 234)
