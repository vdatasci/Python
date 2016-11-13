import numpy as np
import pandas as pd

df = pd.DataFrame(dict(A = np.array(['foo','bar','bah','foo','bar'])))

df['A'].iloc[0] = np.nan
df

#      A
# 0  NaN
# 1  bar
# 2  bah
# 3  foo
# 4  bar
