'''
Author: Jelle Manders
Date: 2021-04-22
File: Blur.py
'''

import YUV
import numpy as np

def blur_mean_ratio(width, height, path):
	"""
	Calculates the video blur mean and ratio for each frame in a given video, 
		and averages these as the return value.
	Args:
		width - The width of each frame in the given video file
		height - The height of each frame in the given video file
		path - The relative path to the source file. File must be of .yuv type, generated with the yuv420p pixel format.
	Return:
		(mean, ratio) - The average blur mean and the average blur ratio
	"""

	# construct a generator that yields a 2D array containing the Y-values of every pixel in each frame
	Y_channel = YUV.Ychann_frame_gen(width, height, path)
	# Let's first build a structure that can go thorugh the motions for one frame, then we can extrapolate on that
	frame = next(Y_channel)
	# Calculate the horizontal and vertical pixel differences
	(Diff_hor, Diff_ver) = calc_pixel_diff(frame)
	# Calculate the horizontal and vertical difference means
	Diff_hor_mean = (1/(height*width)) * np.sum(Diff_hor)
	Diff_ver_mean = (1/(height*width)) * np.sum(Diff_ver)
	# Identify the edge pixel candidates
	Edge_cand_hor = edge_candidates(Diff_hor, Diff_hor_mean)
	Edge_cand_ver = edge_candidates(Diff_ver, Diff_ver_mean)
	# Extract the actual edge pixels
	Edge_pixels_hor, Edge_pixels_ver = edge_pixels(Edge_cand_hor, Edge_cand_ver)
	# The actual edges are either vertical or horizontal, apply elementwise OR to find the actual edges
	Edge_pixels = Edge_pixels_hor | Edge_pixels_ver
	# When calculating the blur of the frame, we need to define a threshold, given to be 0.1 in Vega_2017-PhD_Thesis
	threshold = 10
	# Calculate the horizontal and vertical blur per pixel
	Blur_hor, Blur_ver, Inv_blur_index, Blur_pixels = pixel_blur(frame, Diff_hor, Diff_ver, threshold, Edge_pixels)
	# Calculate the blur mean by dividing the sum of the blur index by the number of blur instances
	Blur_mean = np.sum(Inv_blur_index)/np.sum(Blur_pixels)
	# Calculate the Blur ratio by dividing the amount of blurs by the amount of edges
	Blur_ratio = np.sum(Blur_pixels)/np.sum(Edge_pixels)
	# return result
	return [Blur_mean, Blur_ratio]

def pixel_blur(frame, Diff_hor, Diff_ver, threshold, Edge_pixels):
	# get the dimensions of the frame
	(height, width) = frame.shape
	# construct four 2D matrices with the same dimensions as the frame to store the results
	Blur_hor        = np.zeros((height,width))
	Blur_ver        = np.zeros((height,width))
	Inv_blur_index  = np.zeros((height,width))
	Blur_pixels     = np.zeros((height,width))
	# loop through every pixel
	for i in range(height):
		for j in range(width):
			# we only check edge pixels for blurriness
			if Edge_pixels[i,j] == 1:
				# calculate the horizontal and vertical blur by comparing them with the frame
				Blur_hor[i,j] = abs(frame[i,j] - 0.5*Diff_hor[i,j])/(0.5*Diff_hor[i,j])
				Blur_ver[i,j] = abs(frame[i,j] - 0.5*Diff_ver[i,j])/(0.5*Diff_ver[i,j])
				# The Inverse Blurriness index is the higher of the horizontal and vertical blur
				Inv_blur_index[i,j] = max(Blur_hor[i,j], Blur_ver[i,j])
				# The blurring threshold is applied, leaving only ones and zeroes where blur is or isnt in the frame
				Blur_pixels[i,j] = 1 if Inv_blur_index[i,j] < threshold else 0
	# return all four of the constructed matrices
	return Blur_hor, Blur_ver, Inv_blur_index, Blur_pixels

# def edge_candidates_depr(Diff_matrix, Diff_mean):
# 	(height, width) = Diff_matrix.shape
# 	candidates = np.zeros((height,width), dtype='uint16')
# 	for i in range(height):
# 		for j in range(width):
# 			value = candidates[i][j]
# 			candidates[i][j] = value if value > Diff_mean else 0

def edge_candidates(Diff_matrix, Diff_mean):
	# The edge candidates are those where the value in the Diff_matrix are higher than the value of Diff_mean. To filter all of the Differences lower than the mean, construct a matrix of the same shape as the differences matrix, and fill it with the mean. Then, element-wise compare the differences with the means, resulting in a boolean matrix, which also evaluates to 0 and 1. Each denotes the location of a value higher than the mean. If we then multiply the locations with the differences, every value lower than the mean will be multiplied by zero, while the higher values are left intact.
	Diff_mean_matrix = np.full(Diff_matrix.shape, Diff_mean, dtype='uint16')
	candidate_locations = Diff_matrix > Diff_mean_matrix
	candidates = np.multiply(Diff_matrix, candidate_locations)
	return candidates

def edge_pixels(cand_hor, cand_ver):
	# get the dimensions of the frame
	(height, width) = cand_hor.shape
	# construct two 2D matrices with the same dimensions as the frame to store the results
	horizontal = np.zeros((height,width), dtype='uint16')
	vertical   = np.zeros((height,width), dtype='uint16')
	# loop through every pixel
	for i in range(height):
		for j in range(width):
			# calculate the index of the pixel to your up, right, down, and left, handle edge cases
			up    = i+1 if i+1 < height else i
			right = j+1 if j+1 < width else j
			down  = i-1 if i-1 >= 0 else 0
			left  = j-1 if j-1 >= 0 else 0
			# get the values of the frame at these indexes, convert to in to to prevent ubyte overflow
			up    = int(cand_ver   [up]     [j])
			right = int(cand_hor    [i] [right])
			down  = int(cand_ver [down]     [j])
			left  = int(cand_hor    [i]  [left])
			# for each pixel, calculate the horizontal difference and store it in the result
			horizontal[i,j] = 1 if (cand_hor[i,j] > right and cand_hor[i,j]) > left else 0
			vertical[i,j]   = 1 if (cand_ver[i,j] > up    and cand_ver[i,j]) > down else 0
	# return the filled in horizontal difference matrix
	return (horizontal, vertical)

def calc_pixel_diff(frame):
	"""
	Calculates the horizontal and vertical pixel differences for a given frame, conform the below formula:
		hor: ForAll(i,j) c (Width, Height) => (D_h (i, j) = |f (i, j + 1) − f (i, j − 1)|
		ver: ForAll(i,j) c (Width, Height) => (D_h (i, j) = |f (i + 1, j) − f (i - 1, j)|
	If an index is out of bounds, we handle edges by extending them (e.g. frame[-1][7] becomes frame[0][7])

	Args:
		frame - a 2D Numpy array containing a value for every pixel in the frame
	Return:
		(horizontal, vertical)
		a tuple containing two 2D Numpy arrays, each containing the difference of every Pixel in the frame. The first containing the horizontal, and the second the vertical differences.
	"""
	# get the dimensions of the frame
	(height, width) = frame.shape
	# construct two 2D matrices with the same dimensions as the frame to store the results
	horizontal = np.zeros((height,width), dtype='uint16')
	vertical   = np.zeros((height,width), dtype='uint16')
	# loop through every pixel
	for i in range(height):
		for j in range(width):
			# calculate the index of the pixel to your up, right, down, and left, handle edge cases
			up    = i+1 if i+1 < height else i
			right = j+1 if j+1 < width else j
			down  = i-1 if i-1 >= 0 else 0
			left  = j-1 if j-1 >= 0 else 0
			# get the values of the frame at these indexes, convert to in to to prevent ubyte overflow
			up_value    = int(frame   [up]     [j])
			right_value = int(frame    [i] [right])
			down_value  = int(frame [down]     [j])
			left_value  = int(frame    [i]  [left])
			# for each pixel, calculate the horizontal difference and store it in the result
			horizontal[i,j] = abs(right_value - left_value)
			vertical[i,j]   = abs(up_value    - down_value)
			# We will later be dividing by these numbers, make sure there are no zeros in this matrix
			if horizontal[i,j] == 0: horizontal[i,j] = 1 
			if vertical[i,j] == 0: vertical[i,j] = 1  
	# return the filled in horizontal difference matrix
	return (horizontal, vertical)

# Y_gen = YUV.Ychann_frame_gen(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
# for f in Y_gen:
# 	print("regular frame:")
# 	print(f)
# 	(h,v) = calc_pixel_diff(f)
# 	break

# print("horizontal diff:")
# print(h)
# print("vertical diff:")
# print(v)