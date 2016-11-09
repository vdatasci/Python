from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print i
# 1
# 2
# 3
# a
# b
# c
###


from itertools import *

for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
# (1, 'a')
# (2, 'b')
# (3, 'c')
###






from itertools import *

print 'Stop at 5:'
for i in islice(count(), 5):
    print i

print 'Start at 5, Stop at 10:'
for i in islice(count(), 5, 10):
    print i

print 'By tens to 100:'
for i in islice(count(), 0, 100, 10):
    print i




## TO BE CONTINUED...
