class logger:
    def __init__(self):
            self.data = []
    def __getitem__(self, key):
            return self.data[key]
    def __call__(self, item):
            self.data.append(item)
