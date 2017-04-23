def standard_deviation(l):
    return (sum([(x-sum(l)/len(l))**2 for x in l])/len(l))**(0.5)
