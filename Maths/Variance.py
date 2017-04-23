def variance(l):
    return sum([(x-sum(l)/len(l))**2 for x in l])/len(l)
