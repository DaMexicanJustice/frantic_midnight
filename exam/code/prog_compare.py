import cv2
import sys
import os
import math

tolerance = 32

def compare(firstpic, secondpic):
	sum = 0 # summed difference
	imga = cv2.imread(firstpic)
	imgb = cv2.imread(secondpic)
	
	for y in range (50):
		for x in range (50):
			pxa = imga[x,y]
			pxb = imgb[x,y]
			
			r2 = int(pxa[0]/tolerance)
			r1 = int(pxb[0]/tolerance)
			g2 = int(pxa[1]/tolerance)
			g1 = int(pxb[1]/tolerance)
			b2 = int(pxa[2]/tolerance)
			b1 = int(pxb[2]/tolerance)
			
			sum += math.sqrt(((r2-r1)**2)+((g2-g1)**2)+((b2-b1)**2)) # euclidian distance
	return sum

if __name__ == "__main__":
	args = sys.argv
	
	if(len(args) < 3):
		print("Usage: python " + args[0] + " (filea) (fileb)")
	else:
		difference = compare(args[1], args[2])
		print("The difference is " + str(difference))
