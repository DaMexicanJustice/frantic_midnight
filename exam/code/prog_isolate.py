import cv2
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

def read(path, switch_channels=True):
	image = cv2.imread(path)
	if switch_channels:
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return image

def create_plot(image, title="untitled"):
	#cv2.imshow("Sample", image)
	plt.imread(image)
	plt.title(title)
	plt.axis("off")
	plt.savefig("hello.png")

def create_mask(image, green_lower, green_upper):

	hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
	mask = cv2.inRange(hsv, green_lower, green_upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	return mask

def waitcv():
	while True:
		if cv2.waitKey(5) == 27:
			break
	cv2.destroyAllWindows()

def mark_object(image, mask):
	contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	c = max(contours, key=cv2.contourArea)
	((x, y), radius) = cv2.boundingRect(c)
	cv2.circle(image, (int(x), int(y)), int(radius), (255, 0, 0), 5)
	return image

def find_contours(frame, area):
	arr = []
	cnts = cv2.findContours(frame.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	for c in cnts:
		if cv2.contourArea(c) >= area:
			(x,y,w,h) = cv2.boundingRect(c)
			#print(str(x) + ":" + str(w) + ":" + str(y) + ":" + str(h))
			arr.append((x,y,w,h))
	return arr


if __name__ == "__main__":
	image_path = "biggamehunter.jpg"
	img = read(image_path)
	
	lowerred = np.uint8((20,30,160))
	uperred = np.uint((50,50,240))
	
	
	gray = create_mask(img, cv2.cvtColor(lowerred, cv2.COLOR_RGB2HSV), cv2.cvtColor(uperred, cv2.COLOR_BGR2RGB))

	the_contours = find_contours(gray, 50)
	idx = 0
	for item in the_contours:
		idx += 1
		(x,y,w,h) = item
		print(str(x) + ":" + str(y) + ":" + str(w) + ":" + str(h))
		crop_tmp = img[y:y+h, x:x+w]
		crop_tmp = cv2.cvtColor(crop_tmp, cv2.COLOR_BGR2RGB)
		crop_tmp50x50 = cv2.resize(crop_tmp, (50,50), interpolation=cv2.INTER_AREA)
		cv2.imwrite("crop" + str(idx) + ".jpg", crop_tmp50x50)