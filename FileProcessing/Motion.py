'''
Author: Jelle Manders
Date: 2021-05-07
File: Motion.py
'''

import YUV
import numpy as np
from math import sqrt

def motion_intensity(width, height, path):
	# From the path, instantiate a frame by frame generator
	Y_channel = YUV.Ychann_frame_gen(width, height, path)

	# prepare motion intensity values container.
	motion_container = []

	# We will be comparing each consecutive frame against the last, so get the first frame to get started
	this_frame = next(Y_channel)
	# From here, loop throught the rest of the frames
	for frame in Y_channel:
		# put the fram we were using last in a new var, and label the current frame as this_frame
		last_frame = this_frame
		this_frame = frame

		# elementwise subtract the last frame from this frame, then raise each element to the power of two
		frame_diff_squared = (this_frame - last_frame) ** 2

		# Taking the sum of all of these differences and rooting this, we get the mean squared error of the difference between the frame, which will be our measure for motion intensity. Add it to the container
		motion_container.append(sqrt(np.sum(frame_diff_squared)))

	# the motion intensity of the video is the average of the motion intensity per frame.
	return sum(motion_container)/len(motion_container)

