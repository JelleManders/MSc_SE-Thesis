# UniformityMeasure/metrics.py
# Author: Jelle Manders
# Date: 29-01-2021
#
# main.py contains a set of helper functions that can be used to determine the uniformity of a set of data.

from sklearn.metrics import mean_squared_error
from statistics import mean, stdev

'''
MSQ implements the mean squared error metric, applied to a list of data. The target parameter is an optional argument that denotes the target value of the data. If no target is supplied, MSQ will compute the average and use that instead.
'''
def MSQ(data, target = None):
	# throw a fit if the data is not a match
	if type(data) is not list:
		raise TypeError('provided data is not a list')
	# We haven't been provided a target, calculate average instead
	target = mean(data) if target == None else target

	# sklearn metrics expects a list of targets as long as the data
	target_list = [target] * len(data)

	# Compute the msq and return
	return mean_squared_error(data, target_list)

def std_dev(data, target = None):
	# throw a fit if the data is not a match
	if type(data) is not list:
		raise TypeError('provided data is not a list')
	
	# We have not been provided a target, calc the raw std_dev
	if target == None:
		return stdev(data)
		
	# We have a target, use this in the calculation
	return stdev(data, target)
