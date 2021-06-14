#!/bin/bash
set -e

# Split the ref video in a set amount of sections, requires some editing to do all the work.

# # Handle 25fps and 50fps video's separately
# for ref_yuv in ./ref/*25*.yuv
# do 
# 	# Construct the target path, include the bitrate, the duration, and the part number
# 	res="${ref_yuv%.yuv}_2s_part%01d.yuv"

# 	# Split the video into two fragments, the split should be at frame 125 (half)
# 	ffmpeg -s 768x432 -i "$ref_yuv" -r 25 -codec copy -map 0 -f segment -segment_frames 50,100,150,200 "$res"
# done

# for ref_yuv in ./ref/*50*.yuv
# do 
# 	# Construct the target path, include the bitrate, the duration, and the part number
# 	res="${ref_yuv%.yuv}_2s_part%01d.yuv"

# 	# split the video into two fragments, the split should be at frame 250 (half)
# 	ffmpeg -s 768x432 -i "$ref_yuv" -r 50 -codec copy -map 0 -f segment -segment_frames 100,200,300,400 "$res"
# done 

# mv ./ref/*2s*.yuv "./2s/ref/"





# Split all of the compressed video's into 1 second segments
for btr in "0064k" "0640k" "0768k" "1024k" "2048k" "3072k" "4096k" "5120k"
do
	# First move to the appropriate bitrate directory
	cd "./Compressed/${btr}"/

	# Handle 25fps and 50fps video's separately
	for ref_yuv in ./*25*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_1s_part%01d.yuv"

		# Split the video into two fragments, the split should be at frame 125 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 25 -codec copy -map 0 -f segment -segment_frames 25,50,75,100,125,150,175,200,225 "$res"
	done

	for ref_yuv in ./*50*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_1s_part%01d.yuv"

		# split the video into two fragments, the split should be at frame 250 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 50 -codec copy -map 0 -f segment -segment_frames 50,100,150,200,250,300,350,400,450 "$res"
	done 

	mv ./*1s*.yuv "../../1s/Compressed/${btr}/"
	cd ../..
done


# Split all of the compressed video's into 2 second segments
for btr in "0064k" "0640k" "0768k" "1024k" "2048k" "3072k" "4096k" "5120k"
do
	# First move to the appropriate bitrate directory
	cd "./Compressed/${btr}"/

	# Handle 25fps and 50fps video's separately
	for ref_yuv in ./*25*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_2s_part%01d.yuv"

		# Split the video into two fragments, the split should be at frame 125 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 25 -codec copy -map 0 -f segment -segment_frames 50,100,150,200 "$res"
	done

	for ref_yuv in ./*50*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_2s_part%01d.yuv"

		# split the video into two fragments, the split should be at frame 250 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 50 -codec copy -map 0 -f segment -segment_frames 100,200,300,400 "$res"
	done 

	mv ./*2s*.yuv "../../2s/Compressed/${btr}/"
	cd ../..
done



# Split all of the compressed video's into 5 second segments
for btr in "0064k" "0640k" "0768k" "1024k" "2048k" "3072k" "4096k" "5120k"
do
	# First move to the appropriate bitrate directory
	cd "./Compressed/${btr}"/

	# Handle 25fps and 50fps video's separately
	for ref_yuv in ./*25*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_5s_part%01d.yuv"

		# Split the video into two fragments, the split should be at frame 125 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 25 -codec copy -map 0 -f segment -segment_frames 125 "$res"
	done

	for ref_yuv in ./*50*.yuv
	do 
		# Construct the target path, include the bitrate, the duration, and the part number
		res="${ref_yuv%.yuv}_5s_part%01d.yuv"

		# split the video into two fragments, the split should be at frame 250 (half)
		ffmpeg -s 768x432 -i "$ref_yuv" -r 50 -codec copy -map 0 -f segment -segment_frames 250 "$res"
	done 

	mv ./*5s*.yuv "../../5s/Compressed/${btr}/"
	cd ../..
done


# for btr in "0064k" "0640k" "0768k" "1024k" "2048k" "3072k" "4096k" "5120k"
# do
# 	for ref_yuv in ./ref/*.yuv
# 	do 
# 		# Construct the target mp4 path: strip the .yuv, append the bitrate and mp4 extension
# 		comp_mp4="${ref_yuv%.yuv}_btr${btr}.mp4"
# 		# Compress the reference file using the specified bitrate and target path
# 		ffmpeg -s 768x432 -i "$ref_yuv" -c:v libx264 -b:v "$btr" "$comp_mp4"

# 		# Construct the target yuv path by stripping the .mp4, and appening the .yuv extension
# 		comp_yuv="${comp_mp4%.mp4}.yuv"
# 		# Generate the yuv version of the compressed file
# 		ffmpeg -i "$comp_mp4" "$comp_yuv"

# 		# remove the compressed mp4
# 		rm "$comp_mp4"

# 		# Construct destination path for the compressed yuv by appending the compressed 
# 		# 	and bitrate directories, and stripping the first five characters (./ref/)
# 		comp_yuv_dest="./Compressed/${btr}/${comp_yuv:6}"
# 		# move the compressed yuv to its destination
# 		mv "$comp_yuv" "$comp_yuv_dest"
# 	done 
# done
