from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import numpy as np
import os

    While 0 == 0:

    lst=[]
    lst2=[]

    A = np.matrix([['hip hop','mixcloud'],['music','jammin']])
    print(A)
    srch = raw_input('Whatchu searchin? ')


    i = int(re.search('[0-9]+', str(A.shape)).group(0))
    j = int(re.search(' [0-9]+', str(A.shape)).group(0))
    for row in range(i):
        for col in range(j):
                lst.append(A[row,col])


    for o in range(i+j):
        lst2.append(fuzz.partial_ratio(srch,lst[o]))


    maxlst2index = lst2.index(max(lst2))
    srch_rslt = lst[maxlst2index]
    print(np.where(A==srch_rslt))

    os.system('P:\Python\Projects\Fuzzy-Regex-Searching-on-a-Matrix-to-return-the-Index-and-Value.py')
