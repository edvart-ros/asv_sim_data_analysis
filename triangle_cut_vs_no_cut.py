import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy.interpolate import interp1d 


def PlotSimplerGraph():
	data_cut = pd.read_csv("data/CoarseSphereResults.csv")
	data_no_cut = pd.read_csv("data/CoarseSphereNoCut.csv")

	data_cut = data_cut[data_cut['depth'] <= 1.0]
	data_no_cut = data_no_cut[data_no_cut['depth'] <= 1.0]

	data_cut = data_cut[data_cut['depth'] >= -0.1]
	data_no_cut = data_no_cut[data_no_cut['depth'] >= -0.1]

	R = 0.5
	h_analytical = np.linspace(0, 2*R, 500)
	V_analytical = (np.pi * h_analytical**2 / 3) * (3*R - h_analytical)

	


	# Set font to Times New Roman
	mpl.rcParams['font.family'] = 'Times New Roman'
	mpl.rcParams['font.size'] = 12
	mpl.rcParams.update({'font.size': 12})
	fig, ax = plt.subplots(figsize=(10, 5))
	plt.grid(True)

	ax.plot(
		data_no_cut['depth'], 
		data_no_cut['volume'], 
		color='#ED230B', 
		label='Simulation: 80 triangles without cutting')

	ax.plot(
		data_cut['depth'], 
		data_cut['volume'], 
		color='#0000ff',
		label='Simulation: 80 triangles with cutting')

	ax.plot(
		h_analytical, 
		V_analytical,
		'--',
		color='black',
		label='Analytic')

	ax.set_xlabel('Depth')
	ax.set_ylabel('Displaced Volume')
	ax.legend(loc='upper left')

	ax.set_aspect('equal')
	start, end = 0.0, 1.0  # Assuming you want ticks from 0.0 to 1.0
	start1, end1 = 0.0, 0.7  # Assuming you want ticks from 0.0 to 1.0
	ax.set_xticks(np.arange(start, end + 0.1, 0.1))  # +0.1 to include the end point
	ax.set_yticks(np.arange(start1, end1 + 0.1, 0.1))

	# Define the bounding box for the zoomed-in area
	x1, x2, y1, y2 = 0.90, 1.0, 0.45, 0.53  # Adjust as needed

	# Create inset axes
	axins = inset_axes(
		ax, 
		width="15%", 
		height="90%", 
		loc='lower left',
		bbox_to_anchor=(1.05, 0.04, 1, 1),
		bbox_transform=ax.transAxes)

	# Plot the same data on the inset axes
	axins.plot(
		data_no_cut['depth'], 
		data_no_cut['volume'], 
		color='#ED230B')

	axins.plot(
		data_cut['depth'], 
		data_cut['volume'],
		color='#0000ff')

	axins.plot(
		h_analytical, 
		V_analytical,
		'--',
		color='black')


	# Set the limits for the inset axes to zoom in on the bounding box
	axins.set_xlim(x1, x2)
	axins.set_ylim(y1, y2)
	axins.set_xticks([0.90,0.95, 1.0])
	axins.set_yticks([0.46, 0.47, 0.48,0.49, 0.50,0.51, 0.52])
	axins.tick_params(axis='both', length=2)  # Hide tick marks

	# Move y-axis labels to the right
	axins.yaxis.tick_right()
	axins.yaxis.set_label_position('right')	

  # Add grid lines to the inset axes for better readability
	axins.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)
	# Use mark_inset to draw a box and connect it to the zoomed area
	mark_inset(ax, axins, loc1=2, loc2=3, fc="none", ec="0.5")

	fig.suptitle('Triangle Performance Comparison', fontsize=16)
	plt.savefig('results/New_CutTrianglePlot.pdf', bbox_inches='tight')

PlotSimplerGraph()
