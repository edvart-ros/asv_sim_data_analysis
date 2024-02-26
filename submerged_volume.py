import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy.interpolate import interp1d 


def VoxelModel():
	path = "data/Voxel/"
	data_coarse = pd.read_csv(path +"VolumeData-Sphere81.csv")
	data_semi_coarse = pd.read_csv(path +"VolumeData-Sphere512.csv")
	data_semi_detailed = pd.read_csv(path +"VolumeData-Sphere4154.csv")
	data_detailed = pd.read_csv(path +"VolumeData-Sphere33378.csv")

	R = 0.5
	h_analytical = np.linspace(0, 2*R, 500)
	V_analytical = (np.pi * h_analytical**2 / 3) * (3*R - h_analytical)

	data_coarse = data_coarse[data_coarse['depth'] <= 1.0]
	data_semi_coarse = data_semi_coarse[data_semi_coarse['depth'] <= 1.0]
	data_semi_detailed = data_semi_detailed[data_semi_detailed['depth'] <= 1.0]
	data_detailed = data_detailed[data_detailed['depth'] <= 1.0]

	data_coarse = data_coarse[data_coarse['depth'] >= 0.0]
	data_semi_coarse = data_semi_coarse[data_semi_coarse['depth'] >= 0.0]
	data_semi_detailed = data_semi_detailed[data_semi_detailed['depth'] >= 0.0]
	data_detailed = data_detailed[data_detailed['depth'] >= 0.0]

	mpl.rcParams.update({'font.size': 12})
	fig, ax = plt.subplots(figsize=(10, 5))
	plt.grid(True)

	ax.plot(data_coarse['depth'], data_coarse['volume'], '--', label='Simulation: 81 voxels')
	ax.plot(data_semi_coarse['depth'], data_semi_coarse['volume'], '--', label='Simulation: 512 voxels')
	ax.plot(data_semi_detailed['depth'], data_semi_detailed['volume'], '--', label='Simulation: 4154 voxels')
	ax.plot(data_detailed['depth'], data_detailed['volume'], '--', label='Simulation: 33378 voxels')

	ax.plot(h_analytical, V_analytical, label='Analytic')
	ax.set_xlabel('Depth')
	ax.set_ylabel('Displaced Volume')
	ax.legend()

	# Define the bounding box for the zoomed-in area
	x1, x2, y1, y2 = 0.93, 0.98, 0.45, 0.53  # Adjust as needed

	# Create inset axes
	axins = inset_axes(ax, width="10%", height="90%", loc='lower left',
	                   bbox_to_anchor=(1.05, 0.04, 1, 1),
	                   bbox_transform=ax.transAxes)

	# Plot the same data on the inset axes
	axins.plot(data_coarse['depth'], data_coarse['volume'], '--')
	axins.plot(data_semi_coarse['depth'], data_semi_coarse['volume'], '--')
	axins.plot(data_semi_detailed['depth'], data_semi_detailed['volume'], '--')
	axins.plot(data_detailed['depth'], data_detailed['volume'], '--')
	axins.plot(h_analytical, V_analytical)

	# Set the limits for the inset axes to zoom in on the bounding box
	axins.set_xlim(x1, x2)
	axins.set_ylim(y1, y2)
	axins.set_xticks([0.93, 0.98])
	axins.set_yticks([0.46, 0.48, 0.50, 0.52])
	axins.tick_params(axis='both', length=2)  # Hide tick marks


	# Use mark_inset to draw a box and connect it to the zoomed area
	mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec="0.5")

	plt.savefig("results/VoxelVolumePlot.pdf", bbox_inches='tight')





def KernerModel():
	path = "data/Kerner/"
	data_coarse = pd.read_csv(path +"CoarseSphereResults.csv")
	data_semi_coarse = pd.read_csv(path +"SemiCoarseSphereResults.csv")
	data_semi_detailed = pd.read_csv(path +"SemiDetailedSphereResults.csv")
	data_detailed = pd.read_csv(path +"DetailedSphereResults.csv")

	R = 0.5
	h_analytical = np.linspace(0, 2*R, 500)
	V_analytical = (np.pi * h_analytical**2 / 3) * (3*R - h_analytical)

	data_coarse = data_coarse[data_coarse['depth'] <= 1.0]
	data_semi_coarse = data_semi_coarse[data_semi_coarse['depth'] <= 1.0]
	data_semi_detailed = data_semi_detailed[data_semi_detailed['depth'] <= 1.0]
	data_detailed = data_detailed[data_detailed['depth'] <= 1.0]
	data_coarse = data_coarse[data_coarse['depth'] >= 0.0]
	data_semi_coarse = data_semi_coarse[data_semi_coarse['depth'] >= 0.0]
	data_semi_detailed = data_semi_detailed[data_semi_detailed['depth'] >= 0.0]
	data_detailed = data_detailed[data_detailed['depth'] >= 0.0]

	mpl.rcParams.update({'font.size': 12})
	fig, ax = plt.subplots(figsize=(10, 5))
	plt.grid(True)
	ax.plot(data_coarse['depth'], data_coarse['volume'], '--', label='Simulation: 80 triangles')
	ax.plot(data_semi_coarse['depth'], data_semi_coarse['volume'], '--', label='Simulation: 320 triangles')
	ax.plot(data_semi_detailed['depth'], data_semi_detailed['volume'], '--', label='Simulation: 1280 triangles')
	ax.plot(data_detailed['depth'], data_detailed['volume'], '--', label='Simulation: 5120 triangles')
	ax.plot(h_analytical, V_analytical, label='Analytic')
	ax.set_xlabel('Depth')
	ax.set_ylabel('Displaced Volume')
	ax.legend()

	# Define the bounding box for the zoomed-in area
	x1, x2, y1, y2 = 0.93, 0.98, 0.45, 0.53  # Adjust as needed

	# Create inset axes
	axins = inset_axes(ax, width="10%", height="90%", loc='lower left',
	                   bbox_to_anchor=(1.05, 0.04, 1, 1),
	                   bbox_transform=ax.transAxes)

	# Plot the same data on the inset axes
	axins.plot(data_coarse['depth'], data_coarse['volume'], '--')
	axins.plot(data_semi_coarse['depth'], data_semi_coarse['volume'], '--')
	axins.plot(data_semi_detailed['depth'], data_semi_detailed['volume'], '--')
	axins.plot(data_detailed['depth'], data_detailed['volume'], '--')
	axins.plot(h_analytical, V_analytical)

	# Set the limits for the inset axes to zoom in on the bounding box
	axins.set_xlim(x1, x2)
	axins.set_ylim(y1, y2)
	axins.set_xticks([0.93, 0.98])
	axins.set_yticks([0.46, 0.48, 0.50, 0.52])
	axins.tick_params(axis='both', length=2)  # Hide tick marks


	# Use mark_inset to draw a box and connect it to the zoomed area
	mark_inset(ax, axins, loc1=3, loc2=1, fc="none", ec="0.5")

	plt.savefig("results/submerged_volume_sphere_with_zoom_and_box.pdf", bbox_inches='tight')
	# Interpolation of the analytical solution
	depth_coarse = data_coarse['depth'].to_numpy()
	depth_semi_coarse = data_semi_coarse['depth'].to_numpy()
	depth_semi_detailed = data_semi_detailed['depth'].to_numpy()
	depth_detailed = data_detailed['depth'].to_numpy()

	volume_coarse = data_coarse['volume'].to_numpy()
	volume_semi_coarse = data_semi_coarse['volume'].to_numpy()
	volume_semi_detailed = data_semi_detailed['volume'].to_numpy()
	volume_detailed = data_detailed['volume'].to_numpy()

	V_analytical_interp_coarse = interp1d(h_analytical, V_analytical)(depth_coarse)
	V_analytical_interp_semi_coarse = interp1d(h_analytical, V_analytical)(depth_semi_coarse)
	V_analytical_interp_semi_detailed = interp1d(h_analytical, V_analytical)(depth_semi_detailed)
	V_analytical_interp_detailed = interp1d(h_analytical, V_analytical)(depth_detailed)

	# Calculation of absolute errors
	error_coarse = (volume_coarse - V_analytical_interp_coarse)**2
	error_semi_coarse = (volume_semi_coarse - V_analytical_interp_semi_coarse)**2
	error_semi_detailed = (volume_semi_detailed - V_analytical_interp_semi_detailed)**2
	error_detailed = (volume_detailed - V_analytical_interp_detailed)**2

	rms_coarse = np.sqrt(np.mean(error_coarse))
	rms_semi_coarse = np.sqrt(np.mean(error_semi_coarse))
	rms_semi_detailed = np.sqrt(np.mean(error_semi_detailed))
	rms_detailed = np.sqrt(np.mean(error_detailed))
	print(rms_coarse, rms_semi_coarse, rms_semi_detailed, rms_detailed)


#KernerModel()

VoxelModel()

