import cv2
import matplotlib.pyplot as plt
from time import sleep
import numpy as np
import sys
from prog_isolate import read, create_mask, create_mask_rgb, find_contours
from prog_compare import compare
import os

def printimage(img):
	while True:
		cv2.imshow("aa",img)
		k = cv2.waitKey(0)
		if k == 27:
			cv2.destroyAllWindows()
			break

def get_crop(item, image):
	(x,y,w,h) = item

	crop_tmp = image[y:y+h, x:x+w]
	crop_tmp50x50 = cv2.resize(crop_tmp, (50,50), interpolation=cv2.INTER_AREA)
	return crop_tmp50x50

def compare_against(source_crop, platform):
	comparables = [f for f in os.listdir(platform) if os.path.isfile(os.path.join(platform, f))]
	
	res = []

	smallest_name = "unknown"
	smallest_value = 99999
	
	__test_diff__ = compare(
		source_crop,
		cv2.imread(
			platform + "/" + comparables[0]
		)
	)
	
	if(__test_diff__ > 10000):
		print("probably shit")
		return (smallest_name, smallest_value)

	for item in comparables:	
		diff = compare(
			source_crop,
			cv2.imread(
				platform + "/" + item
			)
		)
		#print("diff is " + str(diff))
		if(diff < smallest_value):
			smallest_value = diff
			smallest_name = item

	return (smallest_name, smallest_value)
	

def try_detect(image_file, lower, upper, path, masktype, erode=0, dilate=0):
	platform_mask = masktype(image_file, lower, upper, erode, dilate)
	platform_contours = find_contours(platform_mask, 50) # prev was 1
	platform_best_match = ("Unknown", 99999)
	
	idx = 0
	
	verygoodfit = 1000
	
	for item in platform_contours:
		idx += 1
		
		print(str(idx) + "/" + str(len(platform_contours)))
		my_crop = get_crop(item, image_file)
		tmpres = compare_against(my_crop, path )
		#print(tmpres)
		if(tmpres[1] < platform_best_match[1]):
			platform_best_match = (tmpres[0], tmpres[1])
		if tmpres[1] < verygoodfit:
			print("Broke because very good fit")
			break
	
	
	return platform_best_match

def print_best_fit(data, platform):
	if(data[1] <= 1000):
		print(platform)
		print(data)
		exit()
	else:
		print("Checked for " + platform)
		print(data)

if __name__ == "__main__":
	args = sys.argv

	if(len(args) < 2):
		print("error")
		exit()
		
	
	image_file = cv2.imread(args[1])
	
	print_best_fit(try_detect(image_file, (20,50,50), (100,255,255), "./realxbox", create_mask, 2, 2), "xbox")
	print_best_fit(try_detect(image_file, (200,200,200), (255,255,255), "./realps", create_mask_rgb, 0, 2), "ps4")