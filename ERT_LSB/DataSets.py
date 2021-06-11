'''
File: DataSets.py
Author: Jelle Manders
Date: 2021-06-01
'''

def data_ref():
	data = [[0.188321357,	0.4056416119],
			[0.2838765279,	0.6024626161],
			[0.1155812187,	0.3005577697],
			[0.3258408137,	0.6713074827],
			[0.2690896701,	0.7989655035],
			[0.1121634656,	0.2727747217],
			[0.160486586,	0.3370926358],
			[0.3131358568,	0.6705603152],
			[0.1941509244,	0.413897016 ],
			[0.3416879694,	0.8664389746]]
	labels = [99.99, 99.84, 99.99, 99.56, 99.99, 99.99, 99.93, 99.82, 99.75, 99.99]
	return (data, labels)

def data_10s():
	data = [[0.188321357, 0.4056416119, 1237.49596, 3.31426, 0.66771, 1.81072, 3769.4859],
			[0.2838765279, 0.6024626161, 1441.81611, 4.47123, 0.5845, 1.86609, 3587.19167],
			[0.1155812187, 0.3005577697, 179.08251, 2.64784, 0.57699, 1.91682, 3093.29189],
			[0.3258408137, 0.6713074827, 4320.06446, 12.00709, 0.5124, 1.84036, 4201.47226],
			[0.2690896701, 0.7989655035, 302.35469, 6.28341, 0.46503, 1.84693, 5064.5879],
			[0.1121634656, 0.2727747217, 68.26772, 2.26945, 0.61351, 1.92037, 2583.35568],
			[0.160486586, 0.3370926358, 120.77913, 4.11476, 0.56885, 1.93366, 3689.89902],
			[0.3131358568, 0.6705603152, 1355.8561, 5.55947, 0.59235, 1.86402, 3798.15436],
			[0.1941509244, 0.413897016, 261.00349, 3.16578, 0.54108, 1.91932, 2940.80613],
			[0.3416879694, 0.8664389746, 330.23412, 5.04058, 0.48301, 1.8949, 4748.96824],
			[0.13315, 1.14463, 111.26992, 1.81484, 0.67786, 1.92544, 3008.88131],
			[0.19202, 0.65187, 948.8471, 3.25088, 0.66512, 1.81884, 3808.02515],
			[0.1918, 0.6013, 975.70099, 3.25482, 0.66502, 1.8172, 3805.43928],
			[0.19759, 0.56189, 1009.13584, 3.26696, 0.66489, 1.81547, 3802.31893],
			[0.18467, 0.40407, 1066.00547, 3.29126, 0.66524, 1.8147, 3794.40779],
			[0.17116, 0.32043, 1093.50972, 3.30602, 0.6657, 1.81398, 3790.67372],
			[0.16142, 0.27033, 1115.3018, 3.3159, 0.66605, 1.81369, 3787.80411],
			[0.15692, 0.24116, 1132.86519, 3.32555, 0.66635, 1.81332, 3786.23882],
			[0.12133, 1.04397, 240.65884, 2.50392, 0.6374, 1.91203, 2471.68059],
			[0.28751, 1.02229, 1119.60904, 3.7672, 0.58259, 1.86716, 3467.49009],
			[0.29365, 0.99956, 1145.37624, 3.79655, 0.58181, 1.86616, 3477.93191],
			[0.28857, 0.90064, 1178.62896, 3.83891, 0.582, 1.86681, 3486.57896],
			[0.28076, 0.72617, 1239.58615, 3.98821, 0.58185, 1.86662, 3503.53658],
			[0.27457, 0.63582, 1269.03867, 4.08979, 0.58127, 1.86685, 3508.72035],
			[0.27036, 0.57688, 1291.4469, 4.15804, 0.5819, 1.86707, 3514.2708],
			[0.26947, 0.53991, 1308.98859, 4.20885, 0.58234, 1.86672, 3518.82958],
			[0.08707, 0.8036, 24.37428, 1.54361, 0.56921, 1.95419, 2609.22937],
			[0.10134, 0.40281, 117.27341, 2.21766, 0.59127, 1.92293, 3039.69719],
			[0.10089, 0.37337, 125.34645, 2.2524, 0.59021, 1.92101, 3043.99934],
			[0.10264, 0.33946, 136.54198, 2.2933, 0.58594, 1.91918, 3050.62208],
			[0.10388, 0.26047, 157.58741, 2.47081, 0.57931, 1.91696, 3060.12363],
			[0.10718, 0.22952, 164.68202, 2.55687, 0.57778, 1.91662, 3064.79623],
			[0.11209, 0.21288, 168.25825, 2.59484, 0.57727, 1.91673, 3067.91391],
			[0.11712, 0.20376, 170.27949, 2.61354, 0.57698, 1.91661, 3069.52081],
			[0.09739, 0.82974, 393.17787, 4.30332, 0.56315, 1.90908, 2517.94613],
			[0.29798, 1.24227, 2823.24406, 9.53479, 0.53203, 1.85953, 3754.71602],
			[0.30657, 1.21642, 2966.25288, 9.8314, 0.53008, 1.85706, 3794.05019],
			[0.31078, 1.12659, 3175.53235, 10.29956, 0.52805, 1.85382, 3852.42837],
			[0.32086, 0.94968, 3566.83259, 11.11977, 0.51936, 1.84701, 3950.5611],
			[0.32556, 0.84888, 3747.36782, 11.43703, 0.51342, 1.84632, 3981.6331],
			[0.32504, 0.77396, 3860.03445, 11.58124, 0.51358, 1.84437, 3996.8581],
			[0.32402, 0.71669, 3940.50831, 11.65722, 0.51375, 1.8435, 4005.49327],
			[0.07785, 0.77035, 24.18304, 1.53767, 0.52799, 1.94905, 2637.66758],
			[0.18091, 1.09036, 122.99355, 3.86533, 0.49703, 1.90616, 4441.15768],
			[0.19043, 1.09088, 134.92925, 4.05114, 0.50372, 1.89963, 4516.81563],
			[0.20579, 1.08627, 154.48392, 4.2991, 0.50392, 1.89054, 4620.91687],
			[0.24155, 1.03033, 201.42396, 4.859, 0.49507, 1.86848, 4812.67837],
			[0.25963, 0.96905, 227.31722, 5.19748, 0.49203, 1.85953, 4896.02617],
			[0.26984, 0.91153, 244.52343, 5.38967, 0.48354, 1.85508, 4940.88968],
			[0.27641, 0.86153, 258.40701, 5.53085, 0.47465, 1.85021, 4973.64296],
			[0.08961, 0.83073, 32.50966, 1.63423, 0.60866, 1.95093, 1858.98302],
			[0.09376, 0.35374, 58.03525, 1.99117, 0.62837, 1.92344, 2392.38615],
			[0.09489, 0.33317, 59.40409, 1.99612, 0.62662, 1.92291, 2415.99783],
			[0.09629, 0.302, 60.9625, 2.01701, 0.62439, 1.92166, 2446.76443],
			[0.10161, 0.24326, 64.20967, 2.11292, 0.6176, 1.92004, 2505.3474],
			[0.10949, 0.22386, 65.40858, 2.16515, 0.61504, 1.91998, 2529.67692],
			[0.11911, 0.21774, 66.02999, 2.20024, 0.61431, 1.91986, 2542.94474],
			[0.12695, 0.21297, 66.4204, 2.22326, 0.61399, 1.91983, 2550.53181],
			[0.16203, 1.36383, 42.49733, 2.71228, 0.58737, 1.95544, 2936.94381],
			[0.15359, 0.51349, 104.89838, 3.92141, 0.56177, 1.9357, 3651.54228],
			[0.15407, 0.48193, 107.01259, 3.96094, 0.56115, 1.93496, 3665.38281],
			[0.15468, 0.43106, 109.49889, 4.0305, 0.56238, 1.93489, 3677.64985],
			[0.15385, 0.3274, 113.15888, 4.09519, 0.5641, 1.93417, 3690.53514],
			[0.15377, 0.28047, 114.41433, 4.11523, 0.56629, 1.93379, 3691.4339],
			[0.1549, 0.2517, 115.27242, 4.11742, 0.56696, 1.9337, 3691.93344],
			[0.15431, 0.2298, 115.99055, 4.11935, 0.56744, 1.93377, 3691.80496],
			[0.15094, 1.40254, 144.04915, 3.05504, 0.58596, 1.92464, 2835.88343],
			[0.34041, 1.24234, 1021.44969, 4.50808, 0.5887, 1.86584, 3603.92938],
			[0.33979, 1.17232, 1056.25777, 4.59283, 0.58818, 1.86501, 3619.66326],
			[0.33365, 1.05312, 1099.82201, 4.76152, 0.58913, 1.86441, 3640.30161],
			[0.3198, 0.829, 1174.50185, 5.10779, 0.59159, 1.86371, 3675.97892],
			[0.31014, 0.72045, 1206.22711, 5.21848, 0.59077, 1.86376, 3687.882],
			[0.30355, 0.65004, 1227.60826, 5.26901, 0.59108, 1.86381, 3695.22373],
			[0.29958, 0.60239, 1243.51746, 5.30525, 0.59134, 1.86365, 3702.102],
			[0.06933, 0.59439, 21.11072, 1.37044, 0.59363, 1.95733, 1394.74653],
			[0.15469, 0.52068, 196.92285, 2.88908, 0.56302, 1.91999, 2762.1972],
			[0.16081, 0.50462, 204.57565, 2.95446, 0.55703, 1.91908, 2797.8942],
			[0.16879, 0.47292, 213.21054, 3.0171, 0.54979, 1.91895, 2835.90676],
			[0.18491, 0.39579, 225.65427, 3.09592, 0.5437, 1.91873, 2874.96163],
			[0.18891, 0.34581, 230.74557, 3.11557, 0.54319, 1.91877, 2884.84314],
			[0.18594, 0.30391, 234.23504, 3.12652, 0.54335, 1.91903, 2890.53778],
			[0.18018, 0.27002, 236.9994, 3.1335, 0.54333, 1.91887, 2895.07888],
			[0.15713, 1.49788, 42.33046, 2.24012, 0.52076, 1.96636, 2415.12845],
			[0.30741, 1.2214, 210.79099, 4.54967, 0.49952, 1.90768, 4629.57358],
			[0.31469, 1.16459, 224.277, 4.63094, 0.49836, 1.90629, 4652.52445],
			[0.32448, 1.07414, 242.01273, 4.72234, 0.49419, 1.90347, 4679.21266],
			[0.32941, 0.83268, 275.04467, 4.83618, 0.48414, 1.89781, 4718.28004],
			[0.31683, 0.68399, 287.75976, 4.90506, 0.48314, 1.89627, 4730.70761],
			[0.30058, 0.58045, 295.46929, 4.95027, 0.48254, 1.89568, 4736.5558],
			[0.28474, 0.50395, 300.8536, 4.97945, 0.48231, 1.89536, 4739.95537]]
	labels = [99.99, 99.84, 99.99, 99.56, 99.99, 99.99, 99.93, 99.82, 99.75, 99.99, 14.12082, 97.98402, 98.83953, 99.44275, 99.9579, 99.98537, 99.98616, 99.98687, 42.15919, 94.11377, 95.04023, 96.12658, 97.92609, 98.53928, 98.89307, 99.09094, 12.08163, 87.61321, 90.95811, 95.0442, 99.52981, 99.87959, 99.95129, 99.97304, 25.14705, 82.08836, 84.75357, 88.34856, 95.06717, 97.1768, 98.02338, 98.40217, 13.06377, 38.03951, 42.58801, 50.84188, 72.65367, 85.08964, 92.44107, 97.17872, 29.75307, 89.23288, 91.2418, 93.79999, 97.64336, 98.84623, 99.33987, 99.58891, 37.55231, 97.13991, 97.79936, 98.5294, 99.28758, 99.48083, 99.57963, 99.64647, 33.00341, 96.18483, 96.93195, 97.69786, 98.56961, 98.85983, 99.00381, 99.0957, 25.81759, 92.43646, 93.51208, 94.77671, 96.67577, 97.28499, 97.658, 97.92822, 21.95518, 84.55241, 88.42094, 93.4294, 99.45584, 99.91981, 99.9796, 99.98773]
	return (data, labels)

def data_10s_excl_ref():
	data = [[0.13315, 1.14463, 111.26992, 1.81484, 0.67786, 1.92544, 3008.88131],
			[0.19202, 0.65187, 948.8471, 3.25088, 0.66512, 1.81884, 3808.02515],
			[0.1918, 0.6013, 975.70099, 3.25482, 0.66502, 1.8172, 3805.43928],
			[0.19759, 0.56189, 1009.13584, 3.26696, 0.66489, 1.81547, 3802.31893],
			[0.18467, 0.40407, 1066.00547, 3.29126, 0.66524, 1.8147, 3794.40779],
			[0.17116, 0.32043, 1093.50972, 3.30602, 0.6657, 1.81398, 3790.67372],
			[0.16142, 0.27033, 1115.3018, 3.3159, 0.66605, 1.81369, 3787.80411],
			[0.15692, 0.24116, 1132.86519, 3.32555, 0.66635, 1.81332, 3786.23882],
			[0.12133, 1.04397, 240.65884, 2.50392, 0.6374, 1.91203, 2471.68059],
			[0.28751, 1.02229, 1119.60904, 3.7672, 0.58259, 1.86716, 3467.49009],
			[0.29365, 0.99956, 1145.37624, 3.79655, 0.58181, 1.86616, 3477.93191],
			[0.28857, 0.90064, 1178.62896, 3.83891, 0.582, 1.86681, 3486.57896],
			[0.28076, 0.72617, 1239.58615, 3.98821, 0.58185, 1.86662, 3503.53658],
			[0.27457, 0.63582, 1269.03867, 4.08979, 0.58127, 1.86685, 3508.72035],
			[0.27036, 0.57688, 1291.4469, 4.15804, 0.5819, 1.86707, 3514.2708],
			[0.26947, 0.53991, 1308.98859, 4.20885, 0.58234, 1.86672, 3518.82958],
			[0.08707, 0.8036, 24.37428, 1.54361, 0.56921, 1.95419, 2609.22937],
			[0.10134, 0.40281, 117.27341, 2.21766, 0.59127, 1.92293, 3039.69719],
			[0.10089, 0.37337, 125.34645, 2.2524, 0.59021, 1.92101, 3043.99934],
			[0.10264, 0.33946, 136.54198, 2.2933, 0.58594, 1.91918, 3050.62208],
			[0.10388, 0.26047, 157.58741, 2.47081, 0.57931, 1.91696, 3060.12363],
			[0.10718, 0.22952, 164.68202, 2.55687, 0.57778, 1.91662, 3064.79623],
			[0.11209, 0.21288, 168.25825, 2.59484, 0.57727, 1.91673, 3067.91391],
			[0.11712, 0.20376, 170.27949, 2.61354, 0.57698, 1.91661, 3069.52081],
			[0.09739, 0.82974, 393.17787, 4.30332, 0.56315, 1.90908, 2517.94613],
			[0.29798, 1.24227, 2823.24406, 9.53479, 0.53203, 1.85953, 3754.71602],
			[0.30657, 1.21642, 2966.25288, 9.8314, 0.53008, 1.85706, 3794.05019],
			[0.31078, 1.12659, 3175.53235, 10.29956, 0.52805, 1.85382, 3852.42837],
			[0.32086, 0.94968, 3566.83259, 11.11977, 0.51936, 1.84701, 3950.5611],
			[0.32556, 0.84888, 3747.36782, 11.43703, 0.51342, 1.84632, 3981.6331],
			[0.32504, 0.77396, 3860.03445, 11.58124, 0.51358, 1.84437, 3996.8581],
			[0.32402, 0.71669, 3940.50831, 11.65722, 0.51375, 1.8435, 4005.49327],
			[0.07785, 0.77035, 24.18304, 1.53767, 0.52799, 1.94905, 2637.66758],
			[0.18091, 1.09036, 122.99355, 3.86533, 0.49703, 1.90616, 4441.15768],
			[0.19043, 1.09088, 134.92925, 4.05114, 0.50372, 1.89963, 4516.81563],
			[0.20579, 1.08627, 154.48392, 4.2991, 0.50392, 1.89054, 4620.91687],
			[0.24155, 1.03033, 201.42396, 4.859, 0.49507, 1.86848, 4812.67837],
			[0.25963, 0.96905, 227.31722, 5.19748, 0.49203, 1.85953, 4896.02617],
			[0.26984, 0.91153, 244.52343, 5.38967, 0.48354, 1.85508, 4940.88968],
			[0.27641, 0.86153, 258.40701, 5.53085, 0.47465, 1.85021, 4973.64296],
			[0.08961, 0.83073, 32.50966, 1.63423, 0.60866, 1.95093, 1858.98302],
			[0.09376, 0.35374, 58.03525, 1.99117, 0.62837, 1.92344, 2392.38615],
			[0.09489, 0.33317, 59.40409, 1.99612, 0.62662, 1.92291, 2415.99783],
			[0.09629, 0.302, 60.9625, 2.01701, 0.62439, 1.92166, 2446.76443],
			[0.10161, 0.24326, 64.20967, 2.11292, 0.6176, 1.92004, 2505.3474],
			[0.10949, 0.22386, 65.40858, 2.16515, 0.61504, 1.91998, 2529.67692],
			[0.11911, 0.21774, 66.02999, 2.20024, 0.61431, 1.91986, 2542.94474],
			[0.12695, 0.21297, 66.4204, 2.22326, 0.61399, 1.91983, 2550.53181],
			[0.16203, 1.36383, 42.49733, 2.71228, 0.58737, 1.95544, 2936.94381],
			[0.15359, 0.51349, 104.89838, 3.92141, 0.56177, 1.9357, 3651.54228],
			[0.15407, 0.48193, 107.01259, 3.96094, 0.56115, 1.93496, 3665.38281],
			[0.15468, 0.43106, 109.49889, 4.0305, 0.56238, 1.93489, 3677.64985],
			[0.15385, 0.3274, 113.15888, 4.09519, 0.5641, 1.93417, 3690.53514],
			[0.15377, 0.28047, 114.41433, 4.11523, 0.56629, 1.93379, 3691.4339],
			[0.1549, 0.2517, 115.27242, 4.11742, 0.56696, 1.9337, 3691.93344],
			[0.15431, 0.2298, 115.99055, 4.11935, 0.56744, 1.93377, 3691.80496],
			[0.15094, 1.40254, 144.04915, 3.05504, 0.58596, 1.92464, 2835.88343],
			[0.34041, 1.24234, 1021.44969, 4.50808, 0.5887, 1.86584, 3603.92938],
			[0.33979, 1.17232, 1056.25777, 4.59283, 0.58818, 1.86501, 3619.66326],
			[0.33365, 1.05312, 1099.82201, 4.76152, 0.58913, 1.86441, 3640.30161],
			[0.3198, 0.829, 1174.50185, 5.10779, 0.59159, 1.86371, 3675.97892],
			[0.31014, 0.72045, 1206.22711, 5.21848, 0.59077, 1.86376, 3687.882],
			[0.30355, 0.65004, 1227.60826, 5.26901, 0.59108, 1.86381, 3695.22373],
			[0.29958, 0.60239, 1243.51746, 5.30525, 0.59134, 1.86365, 3702.102],
			[0.06933, 0.59439, 21.11072, 1.37044, 0.59363, 1.95733, 1394.74653],
			[0.15469, 0.52068, 196.92285, 2.88908, 0.56302, 1.91999, 2762.1972],
			[0.16081, 0.50462, 204.57565, 2.95446, 0.55703, 1.91908, 2797.8942],
			[0.16879, 0.47292, 213.21054, 3.0171, 0.54979, 1.91895, 2835.90676],
			[0.18491, 0.39579, 225.65427, 3.09592, 0.5437, 1.91873, 2874.96163],
			[0.18891, 0.34581, 230.74557, 3.11557, 0.54319, 1.91877, 2884.84314],
			[0.18594, 0.30391, 234.23504, 3.12652, 0.54335, 1.91903, 2890.53778],
			[0.18018, 0.27002, 236.9994, 3.1335, 0.54333, 1.91887, 2895.07888],
			[0.15713, 1.49788, 42.33046, 2.24012, 0.52076, 1.96636, 2415.12845],
			[0.30741, 1.2214, 210.79099, 4.54967, 0.49952, 1.90768, 4629.57358],
			[0.31469, 1.16459, 224.277, 4.63094, 0.49836, 1.90629, 4652.52445],
			[0.32448, 1.07414, 242.01273, 4.72234, 0.49419, 1.90347, 4679.21266],
			[0.32941, 0.83268, 275.04467, 4.83618, 0.48414, 1.89781, 4718.28004],
			[0.31683, 0.68399, 287.75976, 4.90506, 0.48314, 1.89627, 4730.70761],
			[0.30058, 0.58045, 295.46929, 4.95027, 0.48254, 1.89568, 4736.5558],
			[0.28474, 0.50395, 300.8536, 4.97945, 0.48231, 1.89536, 4739.95537]]
	labels = [14.12082, 97.98402, 98.83953, 99.44275, 99.9579, 99.98537, 99.98616, 99.98687, 42.15919, 94.11377, 95.04023, 96.12658, 97.92609, 98.53928, 98.89307, 99.09094, 12.08163, 87.61321, 90.95811, 95.0442, 99.52981, 99.87959, 99.95129, 99.97304, 25.14705, 82.08836, 84.75357, 88.34856, 95.06717, 97.1768, 98.02338, 98.40217, 13.06377, 38.03951, 42.58801, 50.84188, 72.65367, 85.08964, 92.44107, 97.17872, 29.75307, 89.23288, 91.2418, 93.79999, 97.64336, 98.84623, 99.33987, 99.58891, 37.55231, 97.13991, 97.79936, 98.5294, 99.28758, 99.48083, 99.57963, 99.64647, 33.00341, 96.18483, 96.93195, 97.69786, 98.56961, 98.85983, 99.00381, 99.0957, 25.81759, 92.43646, 93.51208, 94.77671, 96.67577, 97.28499, 97.658, 97.92822, 21.95518, 84.55241, 88.42094, 93.4294, 99.45584, 99.91981, 99.9796, 99.98773]
	return (data, labels)