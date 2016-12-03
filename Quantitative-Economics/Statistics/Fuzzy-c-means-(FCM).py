#This code is from the skfuzzy Document. I will be creating a Quantitative Economics example soon.

#Fuzzy c-means (FCM) is a data clustering technique in which a dataset is grouped into n clusters with every datapoint in the dataset belonging to every cluster to a certain degree.

#In marketing, customers can be grouped into fuzzy clusters based on their 
#needs, brand choices, psycho-graphic profiles, or other marketing related partitions.

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']


centers = [[4, 2],
[1, 7],

[5, 6]]


sigmas = [[0.8, 0.3],
[0.3, 0.5],

[1.1, 0.7]]


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

tplotlib.lines.Line2D object at 0x0371BFB0>]
tplotlib.lines.Line2D object at 0x03728150>]
tplotlib.lines.Line2D object at 0x037284B0>]


ax0.set_title('Test data: 200 points x3 clusters.')
plotlib.text.Text object at 0x03703E50>



plt.show()
