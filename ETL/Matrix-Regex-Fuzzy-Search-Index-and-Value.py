from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import numpy as np


A = np.matrix([['hip hop','mixcloud'],['music','jammin']])
A

srch = raw_input('Whatchu searchin? ')

process.extract(srch, A, limit=1)

process.extract(srch, A[0,0], limit=1)

A.shape

#matrix dimension(i,j)
i = int(re.search('[0-9]+', str(A.shape)).group(0))
j = int(re.search(' [0-9]+', str(A.shape)).group(0))

