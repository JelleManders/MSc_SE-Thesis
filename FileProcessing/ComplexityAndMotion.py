import subprocess
import os

def Comp_Motion_comp():
	ref = '../resources/LiveVD/ref/'
	for f in os.listdir(ref):
		framerate = get_fps(f)

		# print("Doing " + f + " at framerate " + framerate + "...")

		for btr in ["0064k", "0640k", "0768k", "1024k", "2048k", "3072k", "4096k", "5120k"]:

			result = subprocess.run(['ffmpeg', 
				'-s', '768x432', 
				'-i', ref+f, 
				'-r', framerate, 
				'-c:v', 'libx264', 
				'-b:v', btr, 
				'../resources/LiveVD/ref/test.mp4'], stderr  = subprocess.PIPE)

			decoded = result.stderr.decode('utf-8')

			subprocess.run(['rm', '../resources/LiveVD/ref/test.mp4'])

			I_QP, I_bits, P_QP, P_bits = read_output(decoded)

			C = I_bits / (2 * 10**6 * 0.91**I_QP)
			M = I_bits / (2 * 10**6 * 0.87**I_QP)

			print(f[:3] + " - " + btr + ":\t" + str(round(C,5)) + "\t" + str(round(M,5)))

def Comp_Motion_ref():
	ref = '../resources/LiveVD/ref/'
	for f in os.listdir(ref):
		framerate = get_fps(f)

		print("Doing " + f + " at framerate " + framerate + "...")

		result = subprocess.run(['ffmpeg', 
			'-s', '768x432', 
			'-i', ref+f, 
			'-r', framerate, 
			'-c:v', 'libx264', 
			'-preset', 'veryslow', 
			'-crf', '17', 
			'../resources/LiveVD/ref/test.mp4'], stderr  = subprocess.PIPE)

		decoded = result.stderr.decode('utf-8')

		subprocess.run(['rm', '../resources/LiveVD/ref/test.mp4'])

		I_QP, I_bits, P_QP, P_bits = read_output(decoded)

		C = I_bits / (2 * 10**6 * 0.91**I_QP)
		M = I_bits / (2 * 10**6 * 0.87**I_QP)

		print("Comp: " + str(C) + ", Mot: " + str(M))
	
def get_fps(path):
	i = path.find('fps')
	return path[i-2:i]

def read_output(output):	
	I_s = output.find('frame I')
	P_s = output.find('frame P')
	B_s = output.find('frame B')

	I_e = output.find("\n", I_s)
	P_e = output.find("\n", P_s)
	B_e = output.find("\n", B_s)

	I = output[I_s:I_e]
	P = output[P_s:P_e]
	B = output[B_s:B_e]

	I_QP, I_bits = get_stats(I)
	P_QP, P_bits = get_stats(P)
	B_QP, B_bits = get_stats(B)

	P_QP = P_QP + B_QP
	P_bits = P_bits + B_bits

	return (I_QP, I_bits, P_QP, P_bits)

def get_stats(data):
	QP_s = data.find('QP:')
	QP_e = data.find('size', QP_s)
	QP = float(data[QP_s+3:QP_e-2])

	Bits_s = data.find('size:')
	Bits = int(data[Bits_s+5:])

	return QP, Bits

Comp_Motion_comp()
