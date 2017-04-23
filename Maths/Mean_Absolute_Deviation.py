
def mean_absolute_deviation(l):
    return sum([abs(x-(sum(l)/len(l))) for x in l])/len(l)
