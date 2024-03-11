import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy.interpolate import interp1d 
from matplotlib.lines import Line2D

#Locations:
path 	= "data/TimingData/"
a 		= path + "TimeData-Voxel_CutSphere1309.csv"
b 		= path + "TimeData-Voxel_NotCutSphere1309.csv"
c 		= path + "TimeData-Submersion-Triangle_Sphere1280.csv"
#d 		= path + "TimeData-Submersion-Triangle_NotCutSphere1280.csv"


# Develop lists from csv
a_list	= pd.read_csv(a)
b_list	= pd.read_csv(b)
c_list	= pd.read_csv(c)
#d_list 	= pd.read_csv(d)

# Isolate values between 0 and 99
a_list = a_list[a_list['iteration_number'] >= 0]
data_voxel_cut = a_list[a_list['iteration_number'] <= 99]

b_list = b_list[b_list['iteration_number'] >= 0]
data_voxel_notcut = b_list[b_list['iteration_number'] <= 99]

c_list = c_list[c_list['iteration_number'] >= 0]
data_triangle_cut = c_list[c_list['iteration_number'] <= 99]

#d_list = d_list[d_list['iteration_number'] >= 0]
#data_triangle_notcut = d_list[d_list['iteration_number'] <= 99]


# Set font to Times New Roman
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(figsize=(10, 5))
plt.grid(True)

ax.plot(
	data_voxel_cut['iteration_number'], 
	data_voxel_cut['time'], 
	color='#ED230B', 
	label='1309 cut voxels')

ax.plot(
	data_voxel_notcut['iteration_number'], 
	data_voxel_notcut['time'], 
	color='#0000ff',
	label='1309 voxels')

ax.plot(
	data_triangle_cut['iteration_number'], 
	data_triangle_cut['time'], 
	color='#009b14',
	label='1280 cut triangles')


ax.set_xlabel('Iteration number')
ax.set_ylabel('Time')
#ax.legend(loc='upper left')
ax.set_aspect('auto', adjustable='box')

#ax.set_aspect('equal')
#start, end = 0.0, 1.0  # Assuming you want ticks from 0.0 to 1.0
#start1, end1 = 0.0, 0.7  # Assuming you want ticks from 0.0 to 1.0
#ax.set_xticks(np.arange(start, end + 0.1, 0.1))  # +0.1 to include the end point
#ax.set_yticks(np.arange(start1, end1 + 0.1, 0.1))
ax.set_xticks(np.arange(0, 110, 10)) # Adjust the range and step as needed
ax.set_yticks(np.arange(0, 3000, 500))

labels = ['1309 cut voxels', '1309 voxels', '1280 cut triangles']# '1280 triangles'
custom_lines = [
Line2D([0], [0], color='#ED230B',  lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#0000ff', lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#009b14', lw=0, marker='s', markersize=10)]
#Line2D([0], [0], color='#ffb200', lw=0, marker='s', markersize=10)]

ax.legend(custom_lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=False, ncol=5)


fig.suptitle('Timing Performance Comparison', fontsize=16)
plt.savefig('results/New_TimingPlot.pdf', bbox_inches='tight')