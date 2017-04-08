[i for i,x in enumerate('this is a sentence is this'.split(' ')) if x == 'this']




import numpy as np
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0]





[xv if c else yv for (c,xv,yv) in zip(condition,x,y)]




np.where(np.array('this is a sentence is this'.split(' ')) == 'this')
