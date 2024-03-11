import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy.interpolate import interp1d 
from matplotlib.lines import Line2D



data_empty = pd.read_csv("data/FpsEmptyWorld.csv")
data_ocean = pd.read_csv("data/FpsDefaultOcean.csv")
data_dynamics = pd.read_csv("data/FpsWamvKernerBuoyancyDynamics.csv")
data_camera = pd.read_csv("data/FpsWamvCamera.csv")
data_all_sensors = pd.read_csv("data/FpsWamvAllSensors.csv")

average_empty = np.mean(data_empty[" fps "])
average_ocean = np.mean(data_ocean[" fps "])
average_single_boat = np.mean(data_dynamics[" fps "])
average_sensor_camera = np.mean(data_camera[" fps "])
average_all_sensors = np.mean(data_all_sensors[" fps "])
plt.figure(figsize=(8, 8))  # Set the figure size as a square

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams.update({'font.size': 12})

# Create figure and axes instances
fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size as a square
plt.grid(True)

ax.plot(
	data_empty["Time"], 
	data_empty[" fps "], 
	label =f"Empty World", 
	marker='o',
	color='black')

ax.plot(
	data_ocean["Time"], 
	data_ocean[" fps "], 
	label = "Ocean only", 
	marker='o',
	color='#0000ff')

ax.plot(
	data_dynamics["Time"], 
	data_dynamics[" fps "], 
	label = "With single boat", 
	marker='o',
	color='#009b14')

ax.plot(
	data_camera["Time"], 
	data_camera[" fps "], 
	label = "With sensor camera", 
	marker='o',
	color='#ffb200')

ax.plot(
	data_all_sensors["Time"], 
	data_all_sensors[" fps "], 
	label = "With all sensors",
	marker='o',
	color='#ED230B')
	#, linewidth=2, )


#plt.legend()
#ax.legend(bbox_to_anchor=(1.05, 1),loc='upper left', borderaxespad=0.)
#plt.aspect('equal')

# Add grid, labels, and title
#plt.grid(True)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frames per Second (FPS)')

# Set y-limits and add a tight layout
ax.set_ylim((0, 450))
ax.set_xlim((0, 15))
ax.set_xticks(np.arange(0, 16, 1))
#plt.tight_layout()

# Set the aspect of the plot to be equal
ax.set_aspect('auto', adjustable='box')

# Create custom legend entries
labels = ['Empty World', 'Ocean only', 'With single boat', 'With sensor camera', 'With all sensors']
custom_lines = [
Line2D([0], [0], color='black',  lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#0000ff', lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#009b14', lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#ffb200', lw=0, marker='s', markersize=10),
Line2D([0], [0], color='#ED230B', lw=0, marker='s', markersize=10)]

ax.legend(custom_lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=False, ncol=5)
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=False, ncol=5) 


fig.suptitle("Simulation Performance", fontsize=16)
plt.savefig("results/New_PerformancePlot.pdf", bbox_inches='tight')