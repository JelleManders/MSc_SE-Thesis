'''
Author: Jelle Manders
Date: 2021-05-07
File: Blockiness.py
'''

import numpy as np
import YUV
from Tools import convolve_2d_3x3

np.set_printoptions(threshold=np.inf)

def blockiness(width, height, path):
	# To determine the blockiness of a video, we will be applying Sobel operators to the frame
	# Construct one for the horizontal and one for the vertical edges. the vertical is simply the transpose of the horizontal
	S_h = np.array( [
			[-1, -2, -1],
			[ 0,  0,  0],
			[ 1,  2,  1]
		] )
	S_v = np.transpose(S_h)
	# Later on we will need the indices of all the inner pixels of an 8x8 block. This is predefined here.
	inn_ind = [ (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
			    (2,1),                        (2,6),
			    (2,1),                        (3,6),
			    (2,1),                        (4,6),
			    (5,1),                        (5,6),
	            (6,1),(6,2),(6,3),(6,4),(6,5),(6,6) ]
	# Instantiate an accumulator for the blockiness measure per frame
	Accum_blockiness = []
	# create a frame-by-frame generator from the given path
	Y_channel = YUV.Ychann_frame_gen(width, height, path)

	framenum = 0
	# Loop through each frame
	for frame in Y_channel:
		framenum += 1
		# print("Doing frame " + str(framenum) + "...")
		# Obtain the horizontal and vertical edges by applying the Sobel operators respectively
		E_h = convolve_2d_3x3(frame, S_h)
		E_v	= convolve_2d_3x3(frame, S_v)
		# Later in the calculation we will need the maximum value of both of these
		E_h_max = np.max(E_h)
		E_v_max = np.max(E_v)
		# We will compute the blockiness by measuring the distortion of each 8x8 pixel block, instantiate an accumulator for the results
		Accum_distortion = []
		# First cut the larger matrix into rows with a height of eight pixels
		for rows_h, rows_v in zip(np.split(E_h, height/8, axis=0), np.split(E_v, height/8, axis=0)):
			# Then split into 8x blocks
			for block_h, block_v in zip(np.split(rows_h, width/8, axis=1), np.split(rows_v, width/8, axis=1)):
				# Calculate the distortion level for each block
				distortion = calc_distortion(block_h, block_v, E_h_max, E_v_max, inn_ind)
				# append the distortion of this block to the accumulator, if it is a suitable number.
				if distortion >= 0:
					Accum_distortion.append(distortion)
		# Now that we have found the distortion for each block, we can compute the blockiness for the frame. This is the average distortion per block. Add this value to the accumulator
		Accum_blockiness.append(sum(Accum_distortion) / len(Accum_distortion))
	# Finally, the video blockiness is the average frame blockiness
	return sum(Accum_blockiness) / len(Accum_blockiness)

def calc_distortion(block_h, block_v, E_h_max, E_v_max, inn_ind):
	# The boundary block edges are computed by summing all of the blocks values in the far right and far left column for the vertical, and by summing the values in the top and bottom row for the horizontal. This value is then divided by the amount of edge pixels (16) and the max edge value in the frame to reach a value in the range [0,1]. This is achieved by taking the dot product with a well chosen vector, and making the appropriate divisions. For the horizontal lines we take the transpose of th block to ensure the right values are multiplied by the vector.
	B_v = sum(block_v.dot([1,0,0,0,0,0,0,1])) / (16 * E_h_max)
	B_h = sum(np.transpose(block_h).dot([1,0,0,0,0,0,0,1])) / (16 * E_v_max)
	# The block's overall edge value is the maximum of the above two
	B_edge = max(B_h, B_v) if B_h != 0 or B_v != 0 else 1

	# To calculate the values of the inner edges, we will first calculate the inner edge block. we achieve this by elementwise squaring both blocks, adding them together, and taking the element wise square root.
	block_inner = (block_h ** 2 + block_v ** 2) ** 0.5
	block_inner_max = np.max(block_inner) if np.max(block_inner) != 0 else 1
	# The inner edge value is the sum of all the values at the inner indices of the block, and the same as the edges divide by the max value and the amount of indices (16 in this case)
	I_edge = sum( [block_inner[i,j] for i,j in inn_ind] ) / (20 * block_inner_max)

	# print(B_edge, I_edge) 

	# calculate and return the distortion using the edge and inner values. the raising of powers in floating point world seems to carry some risks, do this safely in pwr()
	# return 2 * abs(pwr(B_edge) - pwr(I_edge)) / abs(pwr(B_edge) + pwr(I_edge))
	numerator = abs(B_edge ** 2 - I_edge ** 2)
	denominator = abs(B_edge ** 2 + I_edge ** 2)

	# Apparently it can happen that the sum of the edges is exactly zero, in this case we leave out the datapoint to prevent cascading errors. return negative one to indicate error.
	if denominator == 0.0:
		return -1

	return 2 * numerator / denominator

def pwr(n):
	# Floating poinnt imprecision causes some numbers to return complex when powered with floating points. We only want the real parts, complex parts are negligibly small
	r = n ** 2.3
	if np.iscomplex(r):
		print("Complex found:")
		print(n, r)
		return np.real(r)
	return r
