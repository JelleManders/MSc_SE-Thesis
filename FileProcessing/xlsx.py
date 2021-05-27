# FileProcessing/xlsx.py
# Author: Jelle Manders
# Date: 2021-01-29

# Fileprocessing offers tools to interpret files, this file specialises in xlsx files.

'''

'''
def xlsxReader(path, delim = ';'):
	f = open(path, 'r')
	print(f.readline())


xlsxReader("../resources/GamingVideoSET/Results/PerFrameResults/VMAF_Individual_Final_576.xlsx")