#Linear Regression statistics is a way to extrapolate data and predict the value of dependent variables; Linear Regression shows the relationship between independent variable and dependant variables.

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,10]

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 
# fit_fn is now a function which takes in x and returns an estimate for y

#Chart formatting
plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
plt.xlim(0, 5)
plt.ylim(0, 12)

plt.show()
