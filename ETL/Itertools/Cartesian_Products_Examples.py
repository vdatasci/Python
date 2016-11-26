import itertools

def product(*args, **kwds):
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

#

print(list(product('ABCD','xy')))
# [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'),('D', 'x'), ('D', 'y')]

#

import itertools as it
for thing in it.product('ABCD','xy'):
    print thing  
#('A', 'x')
#('A', 'y')
#('B', 'x')
#('B', 'y')
#('C', 'x')
#('C', 'y')
#('D', 'x')
#('D', 'y')

#

import itertools as it
for thing in it.product('ABCD','xy'):
    print thing[0]+thing[1]
#Ax
#Ay
#Bx
#By
#Cx
#Cy
#Dx
#Dy
