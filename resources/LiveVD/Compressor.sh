#!/bin/bash
set -e

# This script will go through the list of reference videos, and a set of bitrates to compress with. For each bitrate and each file, it will:
# 	- Compress the ref file using a given bitrate, creating an mp4 version of the file
# 	- Parse the mp4 to translate it back into a yuv
# 	- Move the newly generated file to its proper directory
# 	- Remove the no longer needed mp4

for btr in "0064k" "0640k" "0768k" "1024k" "2048k" "3072k" "4096k" "5120k"
do
	for ref_yuv in ./ref/*.yuv
	do 
		# Construct the target mp4 path: strip the .yuv, append the bitrate and mp4 extension
		comp_mp4="${ref_yuv%.yuv}_btr${btr}.mp4"
		# Compress the reference file using the specified bitrate and target path
		ffmpeg -s 768x432 -i "$ref_yuv" -c:v libx264 -b:v "$btr" "$comp_mp4"

		# Construct the target yuv path by stripping the .mp4, and appening the .yuv extension
		comp_yuv="${comp_mp4%.mp4}.yuv"
		# Generate the yuv version of the compressed file
		ffmpeg -i "$comp_mp4" "$comp_yuv"

		# remove the compressed mp4
		rm "$comp_mp4"

		# Construct destination path for the compressed yuv by appending the compressed 
		# 	and bitrate directories, and stripping the first five characters (./ref/)
		comp_yuv_dest="./Compressed/${btr}/${comp_yuv:6}"
		# move the compressed yuv to its destination
		mv "$comp_yuv" "$comp_yuv_dest"
	done 
done