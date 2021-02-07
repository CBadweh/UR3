#!/usr/bin/env python3

# Opencv 1.Find difference between two images 
#		 2. filter color
#		 3. Run SIFT

# Load 2 images. 1 image w/o obj 2 image w/ obj
	# image location: UR3/ default_view.jpg
# Publish object of interested topic:
# Purpose: 

# Resources used: 
# Finding difference between two image:
# 	https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
# Detecting color: 
#	https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
# SIFT:


import rospy
import sys
import cv2
import cv2.xfeatures2d
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

from skimage.measure import compare_ssim
import argparse
import imutils


RGB_image = None

def callbackRGB(data):

	# convert ROS image to OpenCV Image 
	global RGB_image
	bridge = CvBridge()
	RGB_image = bridge.imgmsg_to_cv2(data, "bgr8")




if __name__ == '__main__':

	rospy.init_node('background_subtract')
	rospy.Subscriber('/camera/color/image_raw', Image, callbackRGB)

	#======= Loading images ====================
	default_view = cv2.imread('/home/cbadweh/UR3/default_view.jpg')
	default_view_copy = default_view.copy()
	Object_videw = cv2.imread('/home/cbadweh/UR3/view_with_object.jpg')

	# wait for image to arrive to node
	rate = 100
	r = rospy.Rate(rate)
	while RGB_image is None:
		print("Waiting for color image")
		r.sleep()



	# start streaming 
	while True:

# ============================================================= 
# Image Segmentation 
#==============================================================


		#==== convert the images to grayscale ==============
		grayA = cv2.cvtColor(default_view, cv2.COLOR_BGR2GRAY)
		grayB = cv2.cvtColor(Object_videw, cv2.COLOR_BGR2GRAY)

		#==== compute the Structural Similarity Index =============
		# (SSIM) between the two
		# images, ensuring that the difference image is returned
		(score, diff) = compare_ssim(grayA, grayB, full=True)
		diff = (diff * 255).astype("uint8")
		print("SSIM: {}".format(score))

		# === Threshold the difference image=================
		# followed by finding contours to
		# obtain the regions of the two input images that differ
		thresh = cv2.threshold(diff, 0, 255,
			cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)

		# # loop over the contours, for draing bounding box 
		# for c in cnts:
		# 	# compute the bounding box of the contour and then draw the
		# 	# bounding box on both input images to represent where the two
		# 	# images differ
		# 	(x, y, w, h) = cv2.boundingRect(c)
		# 	cv2.rectangle(default_view, (x, y), (x + w, y + h), (0, 0, 255), 2)
		# 	cv2.rectangle(Object_videw, (x, y), (x + w, y + h), (0, 0, 255), 2)

		ROI = cv2.bitwise_and(Object_videw,Object_videw,mask = thresh)
		ROICopy = ROI.copy()





		# cv2.imshow("default_view", default_view)
		cv2.imshow("Object_videw", Object_videw)
		# # cv2.imshow("RGB_image", RGB_image) # straming video 
		# cv2.imshow("Thresh", thresh)
		cv2.imshow("ROI", ROI)

#============================================================= 
		# Detect color 
#==============================================================

		imageFrame = ROI.copy()

		# Convert the imageFrame in 
		# BGR(RGB color space) to 
		# HSV(hue-saturation-value) 
		# color space 
		hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

		# Set range for red color and 
		# define mask 
		red_lower = np.array([136, 87, 111], np.uint8) 
		red_upper = np.array([180, 255, 255], np.uint8) 
		red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

		# Set range for green color and 
		# define mask 
		green_lower = np.array([25, 52, 72], np.uint8) 
		green_upper = np.array([102, 255, 255], np.uint8) 
		green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

		# Set range for blue color and 
		# define mask 
		blue_lower = np.array([94, 80, 2], np.uint8) 
		blue_upper = np.array([120, 255, 255], np.uint8) 
		blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
		
		# Morphological Transform, Dilation 
		# for each color and bitwise_and operator 
		# between imageFrame and mask determines 
		# to detect only that particular color 
		kernal = np.ones((5, 5), "uint8") 
		
		# For red color 
		red_mask = cv2.dilate(red_mask, kernal) 
		res_red = cv2.bitwise_and(imageFrame, imageFrame, 
								mask = red_mask) 
		
		# For green color 
		green_mask = cv2.dilate(green_mask, kernal) 
		res_green = cv2.bitwise_and(imageFrame, imageFrame, 
									mask = green_mask) 
		
		# For blue color 
		blue_mask = cv2.dilate(blue_mask, kernal) 
		res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
								mask = blue_mask) 

		# Creating contour to track red color 
		contours, hierarchy = cv2.findContours(red_mask, 
											cv2.RETR_TREE, 
											cv2.CHAIN_APPROX_SIMPLE) 
		
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				x, y, w, h = cv2.boundingRect(contour) 
				imageFrame = cv2.rectangle(imageFrame, (x, y), 
										(x + w, y + h), 
										(0, 0, 255), 2) 
				
				cv2.putText(imageFrame, "Red Colour", (x, y), 
							cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
							(0, 0, 255))	 

		# Creating contour to track green color 
		contours, hierarchy = cv2.findContours(green_mask, 
											cv2.RETR_TREE, 
											cv2.CHAIN_APPROX_SIMPLE) 
		
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				x, y, w, h = cv2.boundingRect(contour) 
				imageFrame = cv2.rectangle(imageFrame, (x, y), 
										(x + w, y + h), 
										(0, 255, 0), 2) 
				
				cv2.putText(imageFrame, "Green Colour", (x, y), 
							cv2.FONT_HERSHEY_SIMPLEX, 
							1.0, (0, 255, 0)) 

		# Creating contour to track blue color 
		contours, hierarchy = cv2.findContours(blue_mask, 
											cv2.RETR_TREE, 
											cv2.CHAIN_APPROX_SIMPLE) 
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				x, y, w, h = cv2.boundingRect(contour) 
				imageFrame = cv2.rectangle(imageFrame, (x, y), 
										(x + w, y + h), 
										(255, 0, 0), 2) 
				
				cv2.putText(imageFrame, "Blue Colour", (x, y), 
							cv2.FONT_HERSHEY_SIMPLEX, 
							1.0, (255, 0, 0)) 
				


		# Program Termination 
		cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 




# ============================================================= 
# Image Segmentation 
#==============================================================
		
		
		
		# gray= cv2.cvtColor(ROICopy,cv2.COLOR_BGR2GRAY)
		sift = cv2.SIFT_create()
		kp = sift.detect(ROICopy,None)  # function that find keypoints in the image
		img_kp=cv2.drawKeypoints(ROICopy,kp,None) # Draw small circles o nthe location of keypoints
		# cv2.imwrite('sift_keypoints.jpg',ROICopy)

		# img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		# cv.imwrite('sift_keypoints.jpg',img)

		kp,des = sift.compute(ROICopy,kp)
		cv2.imshow("SIFT_Keypoints", img_kp)












		# press Esc key to exit out of the node 
		if cv2.waitKey(1) == 27:
			break 
	cv2.destoryAllWindows()
