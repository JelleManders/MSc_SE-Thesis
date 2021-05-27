'''
Author: Jelle Manders
Date: 2021-05-07
File: Tools.py
'''

import numpy as np

def laplacian(frame):
	mask = np.array([
			[0,  1, 0],
			[1, -4, 1],
			[0,  1, 0]
		])
	return convolve_2d_3x3(frame, mask)

def avg_filter(frame):
	# Applying an average filter is nothing more than performing a convolution with an all ones 3x3 matrix
	# construct the mask 
	mask = np.ones((3,3), dtype=int)
	# return the convolved matrix
	return convolve_2d_3x3(frame, mask)

def convolve_2d_3x3(matrix, mask):
	# Helper function to perform a convolution of a 3x3 matrix as a mask on a matrix. Edge cases are handled by assuming the edges extend in all directions.
	height, width = matrix.shape
	# instantiate a new matrix to gather the results in
	convolved = np.zeros((height,width))
	# Make sure the given matrix consists of integers so that we can use the necessary maths with it
	m = matrix.astype(int)
	# loop through every pixel
	for i in range(height):
		for j in range(width):
			# calculate the index of the pixel to your up, right, down, and left, handle edge cases
			up    = i+1 if i+1 < height else i
			right = j+1 if j+1 < width else j
			down  = i-1 if i-1 >= 0 else 0
			left  = j-1 if j-1 >= 0 else 0
			# construct a matrix of the area the mask is to be applied to
			this_map = np.array([
				[ m[up,  left], m[up,  j], m[up,  right] ],
				[ m[i,   left], m[i,   j], m[i,   right] ],
				[ m[down,left], m[down,j], m[down,right] ] ])
			# Apply the given mask by performing elementwise multiplication with the map
			result = this_map * mask
			# The value in the convolved matrix is the the sum of the applied mask
			convolved[i,j] = np.sum(result)
	return convolved

# Calculate the absolute path of any LiveVD .yuv file, given wether or not the 
# 	file is a reference file, the category, and the bitrate (if applicable)
def LiveVD_relative_path(ref, cat, btr=None):
	# conversion table for integer representations of btr into the strings used for the paths
	btr_int_to_string = {  64: "0064k",  640: "0640k",  768: "0768k", 1024: "1024k", 
	                     2048: "2048k", 3072: "3072k", 4096: "4096k", 5120: "5120k"}
	if not ref:
		btr = btr_int_to_string[btr]

	# lookup table to find the framerate of any given category
	cat_to_fps = {'bs': 25, 'mc': 50, 'pa': 25, 'pr': 50, 'rb': 25, 
	              'rh': 25, 'sf': 25, 'sh': 50, 'st': 25, 'tr': 25}

	# all paths start with the same relative string, append ref or Compressed/{btr}
	path = "../resources/LiveVD/"
	path += "ref/" if ref else "Compressed/" + btr + "/"

	# All paths refer to their framerates, end with yuv or insert the bitrate
	path += cat + "1_" + str(cat_to_fps[cat]) + "fps_768x432"
	if ref:
		path += ".yuv"
	else:
		path += "_btr" + btr + ".yuv"
	return path

# returns a list of tuples containing the matching of categories with their bitrates
def LiveVD_cats():
	return ['bs', 'mc', 'pa', 'pr','rb','rh','sf','sh','st','tr']
# returns list of bitrates
def bitrates():
	return [64, 640, 768, 1024, 2048, 3072, 4096, 5120]

# returns the relative paths of the reference videos of LiveVD
def LiveVD_refs():
	paths = []
	for cat in LiveVD_cats():
			abs_path = LiveVD_relative_path(True, cat)
			paths.append(".." + abs_path[29:])
	return paths

def LiveVD_dis():
	paths = []
	for cat in LiveVD_cats():
		for btr in bitrates():
			paths.append(LiveVD_relative_path(False, cat, btr))
	return paths

def LiveVD_ref_to_dis():
	paths = []
	for cat in LiveVD_cats():
		for btr in bitrates():
			paths.append((LiveVD_relative_path(True, cat), LiveVD_relative_path(False, cat, btr)))
	return paths
