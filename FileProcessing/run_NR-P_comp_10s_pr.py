# from Blur import blur_mean_ratio
from Blur_Laplacian import blur_laplacian
from Noise import noise_mean_ratio
from Motion import motion_intensity
from Blockiness import blockiness

from Tools import LiveVD_dis_cat, t


def run_NR_P_comp_10s_ParkRun():
	log_file = open("Logs/NR-P_comp_10s_pr.txt", "w")
	log_file.write(t() + " > Starting NR-P metrics of Park Run compressed videos...")
	results_file = open("../resources/LiveVD/Scores/NR-P_comp_10s_pr_scores.txt", "w")
	log_file.write(t() + " > Opened results file...")
	for video in LiveVD_dis_cat("pr"):
		try:
			log_file.write(t() + " > Starting analysis of " + video)
			blur = blur_laplacian(768, 432, video)
			log_file.write(t() + " > finished blur: " + str(blur))
			noise_mean, noise_ratio = noise_mean_ratio(768, 432, video)
			log_file.write(t() + " > finished noise: mean = " + str(noise_mean) + ", ratio = " + str(noise_ratio))
			block = blockiness(768,432, video)
			log_file.write(t() + " > finished blockiness: " + str(blockiness))
			motion = motion_intensity(768, 432, video)
			log_file.write(t() + " > finished motion intensity: " + str(motion))
			log_file.write(t() + " > Finished analysis of " + video)

			results_file.write(
				video[37_39] + "\t" + video[-12:-4] + "\t" +
				"Blur:    " + str(round(blur, 5)) + "\t" + 
				"N_mean:  " + str(round(noise_mean, 5)) + "\t" + 
				"N_ratio: " + str(round(noise_ratio, 5)) + "\t" + 
				"Block:   " + str(round(block, 5)) + "\t" + 
				"Motion:  " + str(round(motion, 5)) + "\t"
			)
			log_file.write(t() + " > Wrote results of " + video + " to results file.")
		except Exception as e:
			results_file.write(video[37_39] + "\t" + video[-12:-4] + "\t" + "Error occured: " + str(e))
			log_file.write(t() + " > Error occured on file " + video + ", error message: " + str(e))
	log_file.write(t() + " > Finished analysis of all videos! closing results_file...")
	results_file.close()
	log_file.write(t() + " > Done. Results can be found in ../resources/LiveVD/Scores/NR-P_comp_10s_pr_scores.txt")
