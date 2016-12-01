import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds')
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar();

x = np.array([1, 1, 2, 3, 2, 0])
y = np.array([0, 3, 1, 3, 5, 2])
d = np.stack((x, y))
distance_cost_plot(d)
plt.show()
