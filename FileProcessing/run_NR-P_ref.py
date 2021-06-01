# from Blur import blur_mean_ratio
from Blur_Laplacian import blur_laplacian
from Noise import noise_mean_ratio
from Motion import motion_intensity
from Blockiness import blockiness

from Tools import LiveVD_refs, t

'''
run_NR-P_ref will house all of the non-compression-based metrics. They will be applied to all of the reference videos, analyzing them one by one to construct a vector of values. The order of these metrics is: 
Blur mean, Noise mean and -ratio, Blockiness, and Motion Intensity. Blur ratio and Jerkiness are to be omitted
'''
def run_NR_P_ref():
	log_file = open("Logs/NR-P_ref.txt", "w")
	log_file.write(t() + " > ref: Starting NR-P metrics of reference videos...")
	results_file = open("../resources/LiveVD/Scores/NR-P_ref_scores.txt", "w")
	log_file.write(t() + " > ref: Opened results file...")
	for video in LiveVD_refs():
		try:
			log_file.write(t() + " > ref: Starting analysis of " + video)
			blur = blur_laplacian(768, 432, video)
			log_file.write(t() + " > ref: finished blur: " + str(blur))
			noise_mean, noise_ratio = noise_mean_ratio(768, 432, video)
			log_file.write(t() + " > ref: finished noise: mean = " + str(noise_mean) + ", ratio = " + str(noise_ratio))
			block = blockiness(768,432, video)
			log_file.write(t() + " > ref: finished blockiness: " + str(blockiness))
			motion = motion_intensity(768, 432, video)
			log_file.write(t() + " > ref: finished motion intensity: " + str(motion))
			log_file.write(t() + " > ref: Finished analysis of " + video)

			results_file.write(
				video[24:26] + "\t" + 
				"Blur:    " + str(round(blur, 5)) + "\t" + 
				"N_mean:  " + str(round(noise_mean, 5)) + "\t" + 
				"N_ratio: " + str(round(noise_ratio, 5)) + "\t" + 
				"Block:   " + str(round(block, 5)) + "\t" + 
				"Motion:  " + str(round(motion, 5)) + "\t"
			)
			log_file.write(t() + " > ref: Wrote results of " + video + " to results file.")
		except Exception as e:
			results_file.write("Error occured: " + str(e))
			log_file.write(t() + " > ref: Error occured on file " + video + ", error message: " + str(e))
	log_file.write(t() + " > ref: Finished analysis of all videos! closing results_file...")
	results_file.close()
	log_file.write(t() + " > ref: Done. Results can be found in ../resources/LiveVD/Scores/NR-P_ref_scores.txt")

run_NR_P_ref()