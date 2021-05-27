'''
Author: Jelle Manders
Date: 2021-04-28
File: Noise.py
'''

import YUV
import numpy as np

from Blur import calc_pixel_diff
from Tools import avg_filter

def noise_mean_ratio(width, height, path):
	"""
	Calculates the video noise mean and ratio for each frame in a given video, 
		and averages these as the return value.
	Args:
		width - The width of each frame in the given video file
		height - The height of each frame in the given video file
		path - The relative path to the source file. File must be of .yuv type, generated with the yuv420p pixel format.
	Return:
		(mean, ratio) - The average noise mean and the average noise ratio
	"""
	# construct a generator that yields a 2D array containing the Y-values of every pixel in each frame
	Y_channel = YUV.Ychann_frame_gen(width, height, path)
	# Initiate tow arrays for storing each frames Noise ratio and mean
	noise_ratios = []
	noise_means = []
	# loop over each frame in the video
	for frame in Y_channel:
		# start by applying an averaging filter
		avg_frame = avg_filter(frame)
		# Calculate the horizontal and vertical pixel differences
		(Diff_hor, Diff_ver) = calc_pixel_diff(frame)
		# Calculate the horizontal and vertical difference means
		Diff_hor_mean = (1/(height*width)) * np.sum(Diff_hor)
		Diff_ver_mean = (1/(height*width)) * np.sum(Diff_ver)
		# Obtain Noise candidate
		Nc = noise_candidate(Diff_hor, Diff_ver, Diff_hor_mean, Diff_ver_mean)
		# Determine actual Noise per pixel
		N = noise_decision(Nc)
		# Calculate the Noise mean and Noise Average
		N_mean, N_ratio = calc_noise_mean_ratio(N)
		# add results to the array
		noise_means.append(N_mean)
		noise_ratios.append(N_ratio)
	# Calculate the average noise mean and ratio over the full video
	full_video_noise_mean = sum(noise_means)/len(noise_means)
	full_video_noise_ratio = sum(noise_ratios)/len(noise_ratios)
	#return results
	return full_video_noise_mean, full_video_noise_ratio

def calc_noise_mean_ratio(Noise):
	# First determine the amount of noisy pixels
	N_count = np.count_nonzero(Noise)
	# The Noise mean is the total noise over the amount of noisy pixels
	N_mean = np.sum(Noise)/N_count
	# The Noise ratio is the amount of Noisy Pixels over the amount of pixels
	N_ratio = N_count/Noise.size
	return (N_mean, N_ratio)

def noise_decision(Nc):
	# Calculate the average noise among the candidates, i.e. the sum of the candidates divided by the amount of pixels
	N_avg = sum(Nc)/Nc.size
	Noise_mean_matrix = np.full(Nc.shape, N_avg, dtype='uint16')
	noise_locations = Nc > Noise_mean_matrix
	Noise = np.multiply(Nc, noise_locations)
	return Noise

def noise_candidate(Dh, Dv, Dh_mean, Dv_mean):
	height, width = Dh.shape
	Nc = np.zeros((height, width))
	# loop through every pixel
	for i in range(height):
		for j in range(width):
			# A pixel is a noise candidate if both it's vertical and horizontal differences is bigger than the mean
			if Dh[i,j] <= Dh_mean and Dv[i,j] <= Dv_mean:
				# The noise candidate value is the higher difference
				Nc[i,j] = max(Dh[i,j], Dv[i,j])
	return Nc
