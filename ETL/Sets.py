def difference(l1):
""" return the list with duplicate elements removed """
return list(set(l1))

def intersection(l1, l2):
""" return the intersection of two lists """
return list(set(l1) & set(l2))

def union(l1, l2):
""" return the union of two lists """
return list(set(l1) | set(l2))
