from Blur_Laplacian import blur_laplacian
from Noise import noise_mean_ratio
from Motion import motion_intensity
from Blockiness import blockiness

from multiprocessing import Process

from Tools import LiveVD_dis_cat_segLen, t
	
def run_all_1s():
	bs = Process(target=run_NR_P_comp_1s, args=('bs',))
	mc = Process(target=run_NR_P_comp_1s, args=('mc',))
	pa = Process(target=run_NR_P_comp_1s, args=('pa',))
	pr = Process(target=run_NR_P_comp_1s, args=('pr',))
	rb = Process(target=run_NR_P_comp_1s, args=('rb',))
	rh = Process(target=run_NR_P_comp_1s, args=('rh',))
	sh = Process(target=run_NR_P_comp_1s, args=('sh',))
	sf = Process(target=run_NR_P_comp_1s, args=('sf',))
	st = Process(target=run_NR_P_comp_1s, args=('st',))
	tr = Process(target=run_NR_P_comp_1s, args=('tr',))
	bs.start()
	mc.start()
	pa.start()
	pr.start()
	rb.start()
	rh.start()
	sh.start()
	sf.start()
	st.start()
	tr.start()
	bs.join()
	mc.join()
	pa.join()
	pr.join()
	rb.join()
	rh.join()
	sh.join()
	sf.join()
	st.join()
	tr.join()

def run_NR_P_comp_1s(category):
	log_file = open("Logs/NR-P_comp_1s_" + category + ".txt", "w")
	log_file.write(t() + " > Starting NR-P metrics of 1 second compressed videos..." + "\n")
	results_file = open("../resources/LiveVD/Scores/NR-P_comp_1s_" + category + "_scores.txt", "w")
	log_file.write(t() + " > Opened results file..." + "\n")
	for video in LiveVD_dis_cat_segLen(category, 1):
		try:
			log_file.write(t() + " > Starting analysis of " + video + "\n")
			log_file.flush()
			blur = blur_laplacian(768, 432, video)
			log_file.write(t() + " > finished blur: " + str(blur) + "\n")
			log_file.flush()
			noise_mean, noise_ratio = noise_mean_ratio(768, 432, video)
			log_file.write(t() + " > finished noise: mean = " + str(noise_mean) + ", ratio = " + str(noise_ratio) + "\n")
			log_file.flush()
			block = blockiness(768,432, video)
			log_file.write(t() + " > finished blockiness: " + str(block) + "\n")
			log_file.flush()
			motion = motion_intensity(768, 432, video)
			log_file.write(t() + " > finished motion intensity: " + str(motion) + "\n")
			log_file.write(t() + " > Finished analysis of " + video + "\n")
			log_file.flush()

			results_file.write(
				video + "\t" +
				"Blur:    " + str(round(blur, 5)) + "\t" + 
				"N_mean:  " + str(round(noise_mean, 5)) + "\t" + 
				"N_ratio: " + str(round(noise_ratio, 5)) + "\t" + 
				"Block:   " + str(round(block, 5)) + "\t" + 
				"Motion:  " + str(round(motion, 5)) + "\n"
			)
			results_file.flush()
			log_file.write(t() + " > Wrote results of " + video + " to results file." + "\n")
			log_file.flush()
		except Exception as e:
			results_file.write(video + "\t" + "Error occured: " + str(e) + "\n")
			results_file.flush()
			log_file.write(t() + " > Error occured on file " + video + ", error message: " + str(e) + "\n")
			log_file.flush()
	log_file.write(t() + " > Finished analysis of all videos! closing results_file..." + "\n")
	results_file.close()
	log_file.write(t() + " > Done. Results can be found in ../resources/LiveVD/Scores/NR-P_comp_1s_" + category + "_scores.txt" + "\n")
	log_file.close()

run_all_1s()
