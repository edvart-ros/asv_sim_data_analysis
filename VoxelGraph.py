import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy.interpolate import interp1d 
from matplotlib.lines import Line2D


# List of tuples, each containing an x and y value
points = [
(7.0, 235538, 117),
(6.5, 210137, 129),
(6.0, 192825, 148),
(5.5, 168110, 166),
(5.0, 141018, 184),
(4.5, 121575, 216),
(4.0, 137497, 375), 
(3.5, 157305, 689),
(3.0, 125813, 858),
(2.5, 144084, 1700), 
(2.0, 125175, 3000),
(1.5, 126309, 7500), 
(1.0, 118239, 24000), 
(0.5, 115793, 201000), 
(0.25, 114375, 1600000)
]

x_values, y_values, weights = zip(*points)

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams.update({'font.size': 12})
fig, ax1 = plt.subplots()

# Plot y_values
ax1.scatter(x_values, y_values, color='r')
#ax1.vlines(x_values, 0, y_values, color='black')
ax1.set_xlabel('Diameter of Cubes')
ax1.set_ylabel('Force', color='r')
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()
plt.plot(x_values, y_values, '-r')

# Secondary y-axis for weights
ax2 = ax1.twinx()
ax2.scatter(x_values, weights, color='b')  # Scatter plot for weights
#ax2.vlines(x_values, 0, weights, color='white')
ax2.set_ylabel('Number of Cubes (logarithmic)', color='b')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_yscale('log')  # Set logarithmic scale
plt.plot(x_values, weights, '-b')

for i in range(len(points)):
    xx = [x_values[i], x_values[i]]  # Same x for both points
    yy = [y_values[i], weights[i]]  # y for the first axis, weight for the second axis
    #plt.plot(xx, yy, color='black')

labels = ['Force', 'Number of cubes']# '1280 triangles'
custom_lines = [
Line2D([0], [0], color='r',  lw=0, marker='s', markersize=10),
Line2D([0], [0], color='b', lw=0, marker='s', markersize=10)]

#ax1.legend(custom_lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=False, ncol=5)


fig.suptitle('Voxel size and complexity plot', fontsize=16)
plt.savefig('results/New_VoxelComplexityPlot.pdf', bbox_inches='tight')
