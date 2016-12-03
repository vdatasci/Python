# 3x + y = 9
# x + 2y = 8

import numpy as np

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
x
