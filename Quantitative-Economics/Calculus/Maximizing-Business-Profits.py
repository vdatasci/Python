#Source: http://tutorial.math.lamar.edu/Classes/CalcI/BusinessApps.aspx
#   An apartment complex has 250 apartments to rent.  If they rent x apartments then their monthly profit, in dollars, is given by,
#       -8*(x**2)+3200*x-80000
#   How many apartments should they rent in order to maximize their profit?
###

import sympy
from sympy import *


x=Symbol('x')

solve(diff(-8*(x**2)+3200*x-80000,x), x)
# [200]
#So, it looks like they will generate the most profit if they only rent out 200 of the apartments instead of all 250 of them.
