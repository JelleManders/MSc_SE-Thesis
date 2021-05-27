'''
Date: 2021-04-22
File: Blur.py
'''

import YUV
import numpy as np

from Tools import laplacian

def blur_laplacian(width, height, path):
	Y_channel = YUV.Ychann_frame_gen(width, height, path)

	accum = []

	for frame in Y_channel:

		# apply laplacian to the frame
		applied = laplacian(frame)

		# The variance of the laplacian is our measure
		accum.append(np.var(applied))

	return sum(accum) / len(accum)