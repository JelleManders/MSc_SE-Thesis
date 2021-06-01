# from Blur import blur_mean_ratio
# from Blur_Laplacian import blur_laplacian
# from Noise import noise_mean_ratio
# from Motion import motion_intensity
# from Blockiness import blockiness

from Tools import LiveVD_dis_cat, t


def run_NR_P_test():
	log_file = open("Logs/NR-P_test.txt", "w")
	log_file.write(t() + " > Starting test of NR-P protocols..." + "\n")
	results_file = open("../resources/LiveVD/Scores/NR-P_test.txt", "w")
	log_file.write(t() + " > Opened results file..." + "\n")
	for video in LiveVD_dis_cat("bs"):
		try:
			log_file.write(t() + " > Starting dummy analysis of " + video + "\n")
			blur = "blur_laplacian(768, 432, video)"
			log_file.write(t() + " > finished blur: " + str(blur) + "\n")
			noise_mean, noise_ratio = ("noise_mean_ratio(768, 432, video)", 'test')
			log_file.write(t() + " > finished noise: mean = " + str(noise_mean) + ", ratio = " + str(noise_ratio) + "\n")
			block = "blockiness(768,432, video)"
			log_file.write(t() + " > finished blockiness: " + str(block) + "\n")
			motion = "motion_intensity(768, 432, video)"
			log_file.write(t() + " > finished motion intensity: " + str(motion) + "\n")
			log_file.write(t() + " > Finished analysis of " + video + "\n")

			results_file.write(
				video[37:39] + "\t" + video[-12:-4] + "\t" +
				"Blur:    " + '#data' + "\t" + 
				"N_mean:  " + '#data' + "\t" + 
				"N_ratio: " + '#data' + "\t" + 
				"Block:   " + '#data' + "\t" + 
				"Motion:  " + '#data' + "\n"
			)
			log_file.write(t() + " > Wrote results of " + video + " to results file." + "\n")
		except Exception as e:
			results_file.write(video[37:39] + "\t" + video[-12:-4] + "\t" + "Error occured: " + str(e) + "\n")
			log_file.write(t() + " > Error occured on file " + video + ", error message: " + str(e) + "\n")
	log_file.write(t() + " > Finished dummy analysis of all videos! closing results_file..." + "\n")
	results_file.close()
	log_file.write(t() + " > Done. Results can be found in ../resources/LiveVD/Scores/NR-P_test_scores.txt" + "\n")

run_NR_P_test()