from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
centers = [[4, 2], [1, 7], [5, 6]]
sigmas = [[0.8, 0.3], [0.3, 0.5], [1.1, 0.7]]

np.random.seed(42)
xpts = np.zeros(1)
ypts = np.zeros(1)
labels = np.zeros(1)


for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
    xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))
    ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
    labels = np.hstack((labels, np.ones(200) * i))


fig0, ax0 = plt.subplots()

for label in range(3):
    ax0.plot(xpts[labels == label], ypts[labels == label], '.',
            color=colors[label])


ax0.set_title('Test data: 200 points x3 clusters.')

plt.show()
