'''
Author: Jelle Manders
Date: 2021-04-22
File: YUV.py

This file will contain all necessary functions to read an entire yuv file, and get the pixel by pixel values.
Inspiration taken from Mark Satchel's answer on https://stackoverflow.com/questions/53467655/import-yuv-as-a-byte-array
'''

import numpy as np
import matplotlib.pyplot as plt

def Ychann_frame_gen(width, height, path):
	"""
	Ychann_FrameGen is a generator that yields a 2D Numpy Array for each frame. 
	Each entry in this array represents the Y value of each pixel.

	Args:
		width - The width of each frame in the given video file
		height - The height of each frame in the given video file
		path - The relative path to the source file. File must be of .yuv type, generated with the yuv420p pixel format.
	"""
	# Determine number of pixels per frame
	pixels = width * height
	# Read entire file into YUV
	YUV = np.fromfile(path, dtype='uint8')
	# define a current index pointer
	cur = 0
	# start a loop to go over each frame
	while True:
		# Get the 1-D array containing all Y-values
		Y = YUV[cur:cur+pixels]
		# If our array is empty, we have hit the end of file
		if len(Y) == 0: break
		# return the first frame's Y data, reshaped into a 2D array
		yield Y.reshape(height,width)
		# update the pointer to go to the next frame, take U and V data into account
		cur += pixels + pixels // 2
		
# Y_frame = Ychann_frame_gen(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
# i=0
# for f in Y_frame:
# 	i += 1
# 	plt.imshow(f, cmap='gray')
# 	plt.show()
# 	if i == 3:
# 		break