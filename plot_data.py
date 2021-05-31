import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import linregress
from scipy.optimize import curve_fit


from scripts.math_functions import gaussian, exponential, exponentially_decaying_gaussian, exponentially_decaying_cosine, scale_values_to_unity, exponentially_decaying_sine, linear_function
from scripts.data_handling import compute_background_intensity, adjust_intensity, trim_data, read_data, average_data


def plot_data(x_values, y_values, fit_function=None):

	plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

	plt.plot(x_values, y_values, 'o-', label='Measured Data', color="navy")

	# try:
	# 	background = compute_background_intensity(intensity_values=y_values, frequency_values=x_values, frequency_limit=[0, 2750])
	# except Exception:
	# 	background = 4718883.78
	#
	# y_values = adjust_intensity(intensity_values=y_values, ground_level=background)
	#
	# values_x_filtered, values_y_filtered = trim_data(x_values, y_values, 2700, 2865)
	#
	# popt = curve_fit(fit_function, values_x_filtered, values_y_filtered, p0=[2825, 50, 4000000])
	#
	# function_parameters = popt[0]
	#
	# y_values = fit_function(values_x_filtered, *function_parameters)
	#
	# y_values = adjust_intensity(intensity_values=y_values, ground_level=background)
	#
	# plt.plot(values_x_filtered, y_values, '*:',  color="darkred",
	# 		 label=f'Gaussian Fit with $\mathcal{{N}}(\mu={function_parameters[0]:.2f}, \sigma^2={function_parameters[1]:.2f})$')

	plt.legend()
	plt.grid()

	plt.xlabel("Potential [V]")
	plt.ylabel("Current [A/cm$^{2}$]")

	plt.show()



def main():
	potential, current = read_data("data/GC_OER_Activity.xlsx", data_format='potential')
	plot_data(potential, current)

	potential, current = read_data("data/NiOx_OER_Activity.xlsx", data_format='potential')
	plot_data(potential, current)

	potential, current = read_data("data/NiOx_deposition.xlsx", data_format='potential')
	plot_data(potential, current)

	time, potential, current = read_data("data/Electrolysis_Pt_GC.xlsx", data_format='time')
	plot_data(time, potential)

	time, potential, current = read_data("data/Electrolysis_Pt_Ni(foam).xlsx", data_format='time')
	plot_data(time, potential)


if __name__ == "__main__":
	main()
