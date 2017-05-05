import cv2
import matplotlib.pyplot as plt
from time import sleep

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

def create_ball_mask(image):
	green_lower = (20,100,180)
	green_upper = (60,255,255)
	hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
	mask = cv2.inRange(hsv, green_lower, green_upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	return mask

if __name__ == "__main__":
	image_path = "./verdasco-dubai-2017-thursday.jpg"
	img = read(image_path)
	#cv2.imshow("Image", img)
	cv2.imshow("Im", create_ball_mask(img))

	#create_plot(img)
	#img = cv2.imread(path)



	#cv2.imshow("Image", img)
	while True:
		if cv2.waitKey(5) == 27:
			break
	cv2.destroyAllWindows()
