from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import numpy as np


A = np.matrix([['hip hop','mixcloud'],['music','jammin']])
srch = raw_input('Whatchu searchin? ')

#matrix dimension(i,j)
i = int(re.search('[0-9]+', str(A.shape)).group(0))
j = int(re.search(' [0-9]+', str(A.shape)).group(0))

for row in range(i):
    for col in range(j):
            lst.append(A[row,col])

lst2 = []
for o in range(i+j):
    lst2.append(fuzz.partial_ratio(srch,lst[o]))

maxlst2index = lst2.index(max(lst2))

lst[maxlst2index]
np.where(A==lst[maxlst2index])
