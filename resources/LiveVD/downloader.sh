#!/bin/bash

# loop categories
for cat in "mc" "pa" "rb" "rh" "sf" "st" "tr"
do
	# each category has 16 samples
	for index in {1..16}
	do
		if [[ "$cat" == "mc" ]]; then
			wget --user live_video --password 'al!Sgr8TX' "https://vqdatabase.ece.utexas.edu/research/live/vqdatabase/videos/${cat}%20Folder/${cat}${index}_50fps.yuv"
		else
			# execute wget, use indices and categories to construct the URL
			wget --user live_video --password 'al!Sgr8TX' "https://vqdatabase.ece.utexas.edu/research/live/vqdatabase/videos/${cat}%20Folder/${cat}${index}_25fps.yuv"
		fi
	done

	# make a new directory for this category
	mkdir "${cat}"

	# move all samples to their directory
	mv "${cat}*_25fps.yuv" "$cat/"
done

# these categories are a little special, two folders and 50 fps
for cat in "pr" "sh"
do
	# First 9 samples reside in folder number 1
	for index in {1..9}
	do
		wget --user live_video --password 'al!Sgr8TX' "https://vqdatabase.ece.utexas.edu/research/live/vqdatabase/videos/${cat}1%20Folder/${cat}${index}_50fps.yuv"
	done

	# 10 through 16 reside in folder number 2
	for index in {10..16}
	do
		wget --user live_video --password 'al!Sgr8TX' "https://vqdatabase.ece.utexas.edu/research/live/vqdatabase/videos/${cat}2%20Folder/${cat}${index}_50fps.yuv"
	done

	# move all samples to their newly made directory
	mkdir "${cat}"

	mv "${cat}*_50fps.yuv" "$cat/"
done

# '
# Blue Sky 	= bs,
# Mobile Calendar = mc
# Pedestrian Area = pa
# Park Run 	= pr
# River Bed 	= rb
# Sunflower 	= sf
# Shields 	= sh
# Station 	= st
# Tractor 	= tr
# '