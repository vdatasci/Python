[i for i,x in enumerate('this is a sentence is this'.split(' ')) if x == 'this']


#OR


import numpy as np
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0]
