'''
Author: Jelle Manders
Date: 2021-04-22
File: NR-P.py

This file will contain the overarching function that will call each different No-Reference Pixel based metric, and produce a report per video.
'''

# from Blur import blur_mean_ratio
from Blur_Laplacian import blur_laplacian
from Noise import noise_mean_ratio
from Motion import motion_intensity
from Blockiness import blockiness

from Tools import LiveVD_refs, LiveVD_dis

from YUV import Ychann_frame_gen

import matplotlib.pyplot as plt


def lapl_blur_test():
	print("Testing Blur of Ref:")
	value = blur_laplacian(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
	print(value)
	# for btr in ["0064", "0640", "0768", "1024", "2048", "3072", "4096", "5120"]:
	# 	value = blur_laplacian(768, 432, "../resources/LiveVD/Compressed/" + btr + "k/pa1_25fps_768x432_btr" + btr + "k.yuv")
	# 	print("Blur at " + btr + ": " + str(value))

# lapl_blur_test()

def blockiness_test():
	# block_ref = blockiness(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
	# print("block_ref: " + str(block_ref))
	block_comp = blockiness(768, 432, "../resources/LiveVD/Compressed/0064k/pa1_25fps_768x432_btr0064k.yuv")
	print("block_comp: " + str(block_comp))

# blockiness_test()

def motion_test():
	print("Testing motion intensity, ref video: ")
	motion = motion_intensity(768,  432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
	print(motion)
	for btr in ["0064", "0640", "0768", "1024", "2048", "3072", "4096", "5120"]:
		motion = motion_intensity(768, 432, "../resources/LiveVD/Compressed/" + btr + "k/pa1_25fps_768x432_btr" + btr + "k.yuv")
		print("Values for " + btr + "kbs compressed video:")
		print(motion)

# motion_test()

def noise_test():
	ref = noise_mean_ratio(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
	print("\nTesting noise, values for ref video:")
	print(ref)
	for btr in ["0064", "0640", "0768", "1024", "2048", "3072", "4096", "5120"]:
		compressed = noise_mean_ratio(768, 432, "../resources/LiveVD/Compressed/" + btr + "k/pa1_25fps_768x432_btr" + btr + "k.yuv")
		print("\nValues for " + btr + "kbs compressed video:")
		print(compressed)

"""
Noise test performed on the first ten frames of the Pedestrian Area video:
	Testing noise, values for ref video:
	(2.337714972593105, 0.4662190755208334)
	Values for 0064kbs compressed video:
	(1.6506017003007183, 0.3335072458526234)
	Values for 0640kbs compressed video:
	(2.148472582247292, 0.4507040895061728)
	Values for 0768kbs compressed video:
	(2.153971077894174, 0.45075231481481487)
	Values for 1024kbs compressed video:
	(2.163024335220851, 0.4498061945408951)
	Values for 2048kbs compressed video:
	(2.2020484544915795, 0.4483959056712963)
	Values for 3072kbs compressed video:
	(2.250728093331601, 0.4487919560185186)
	Values for 4096kbs compressed video:
	(2.2974651506358894, 0.4553282937885803)
	Values for 5120kbs compressed video:
	(2.321719287481198, 0.4602439597800926)
"""

# Deprecated in favour of Lapl_blur
# def blur_test():
# 	print("Testing Blur of Ref:")
# 	mean, ratio = blur_mean_ratio(768, 432, "../resources/LiveVD/ref/pa1_25fps_768x432.yuv")
# 	print("mean: " + str(mean) + ", ratio: " + str(ratio))
# 	for btr in ["0064", "0640", "0768", "1024", "2048", "3072", "4096", "5120"]:
# 		mean, ratio = blur_mean_ratio(768, 432, "../resources/LiveVD/Compressed/" + btr + "k/pa1_25fps_768x432_btr" + btr + "k.yuv")
# 		print("Blur at " + btr + " - mean: " + str(mean) + ", ratio: " + str(ratio))

def one_frame():
	Y = Ychann_frame_gen(768, 432, "../resources/LiveVD/Compressed/1024k/pa1_25fps_768x432_btr1024k.yuv")
	img = next(Y)
	plt.imshow(img, cmap='gray')
	plt.show()

run_NR_P_ref()