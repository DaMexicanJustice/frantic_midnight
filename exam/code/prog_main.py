import cv2
import matplotlib.pyplot as plt
from time import sleep
import numpy as np
import sys
from prog_isolate import read, create_mask, find_contours
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
	
	reference = cv2.imread("./realxbox/crop46.jpg")
	
	smallest = {"name": "Unknown", "value": 1000000}
	
	for item in comparables:
		diff = compare(source_crop, cv2.imread(platform + "/" + item))
		
		if(diff < smallest["value"]):
			smallest["name"] = item
			smallest["value"] = diff
	
	#print("----")
	#print(smallest)
	return smallest

if __name__ == "__main__":
	args = sys.argv

	if(len(args) < 2):
		print("error")
		exit()
	
	image_file = cv2.imread(args[1])
	
	xbox_mask = create_mask(image_file, (20,50,50), (100,255,255)) # TODO: Tweak values
	xbox_contours = find_contours(xbox_mask, 1)
	
	xbox_matches = []
	
	xbox_smallest_val = 99999999
	
	for item in xbox_contours:
		print("compare a contour")
		my_crop = get_crop(item, image_file)
		#printimage(my_crop)
		
		#print(compare_against(my_crop, "./realxbox"))
		tmpres = compare_against(my_crop, "./realxbox" )
		
		xbox_matches.append(tmpres)
		#xbox_matches.append(
		#	compare_against(my_crop, "realxbox")
		#)
		#print(xbox_matches)
	
	#print(xbox_matches)
	for x in xbox_matches:
		if x["value"] < xbox_smallest_val:
			xbox_smallest_val = x["value"]
	#print(xbox_smallest_val)
	for x in xbox_matches:
		if x["value"] == xbox_smallest_val:
			print(x)