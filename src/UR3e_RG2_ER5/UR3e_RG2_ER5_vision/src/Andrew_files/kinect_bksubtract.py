#!/usr/bin/env python

"""
kinect_bksubtract: Takes an image of the robot without objects and calibrates so that when anything new is placed in front of the camera it shows up as a mask. Look up image backgorund subtraction if you need help.

This code was originally for a real Kinect_V2 but due too us going into simulation, it is set up with the kinect model in gazebo.

"""

from collections import Counter
import rospy
import time
from sensor_msgs.msg import Image

import time

import cv2
import numpy as np
import sys
import math

#from kinect_smoothing import HoleFilling_Filter, Denoising_Filter
from cv_bridge import CvBridge, CvBridgeError


bridge = CvBridge() #Class used to convert from ROS images to cv2 images
Depth_image = None
RGB_image = None
flag = None
cheight = None
cwidth = None
pName = "kinect_bksubtract: "



# Takes the depth image from ROS and converts to an 8-bit greyscale image
def callbackDepth(data):
	global Depth_image
	global flag
	Depth_image2 = np.asarray(bridge.imgmsg_to_cv2(data, 'passthrough'))
	Depth_image2 = np.nan_to_num(Depth_image2)
	
	#The image comes in as mesurments so you have to normailize them and multiply by 255
	cv2.normalize(Depth_image2, Depth_image2, 0, 1, cv2.NORM_MINMAX)
	Depth_image2 = Depth_image2 * 255.0
	#Converts the image to 8-bit
	Depth_image = np.array(Depth_image2, dtype=np.uint8)
	flag    =   1

# Takes the color image from ROS and converts to a cv2 image	
def callbackRGB(data):
	global RGB_image
	RGB_image = bridge.imgmsg_to_cv2(data, data.encoding)


if __name__ == '__main__':

	#Sets up ROS subscribers and publishers
	
	#hole_filter = HoleFilling_Filter(flag='min')
	rospy.init_node('background_subtract')
	rospy.Subscriber('/kinect2/qhd/image_color', Image, callbackRGB)
	rospy.Subscriber('/kinect2/sd/image_depth', Image, callbackDepth)
	PubDepthImg = rospy.Publisher('depth_image_norm', Image, queue_size=10)
	PubBksubImg = rospy.Publisher('bksub_image', Image, queue_size=10)
	
	#rospy.Subscriber('/kinect2/qhd/image_depth_rect', Image, callbackDepth)
	
	#Waits for Subcribers to pull in images
	rate = 100
	r = rospy.Rate(rate)
	while Depth_image is None:
		print(pName + "Waiting for depth image")
		r.sleep()
	while RGB_image is None:
		print(pName +"Waiting for color image")
		r.sleep()

	#BackgroundSubtractorMOG2 is a class that takes a history of images and builds the background to subtract
	histry = 10 #10 works pretty well. A larger number gets better results but takes longer to image capture
	fgbg = cv2.createBackgroundSubtractorMOG2(history = histry, detectShadows = False)
	
	for x in range(histry):
		flag = 0
		print(pName + "Sample " + str(x) + "!")
		while flag != 1:
			None
		#Depth_image = fill_depth_colorization(RGB_image, Depth_image)
		fgmask = fgbg.apply(Depth_image) #Applies the history images to the BackgroundSubtractorMOG2

	while True:

		fgmask = fgbg.apply(Depth_image, learningRate = 0) # Learning rate needs to be 0 for this part
	
		#cv2.imshow("Color Kinect", RGB_image)
		#cv2.imshow("Depth Kinect", Depth_image)
		#cv2.imshow("DepthSubtract", fgmask)
		#cv2.imshow("DepthSubtractGR", fgmaskGr)
		depth_message = bridge.cv2_to_imgmsg(Depth_image, encoding="passthrough")
		bksub_message = bridge.cv2_to_imgmsg(fgmask, encoding="passthrough")
		try:		
			PubDepthImg.publish(depth_message)
			PubBksubImg.publish(bksub_message)
		except:
			#print("Not Published")
			None
		
		if cv2.waitKey(1) == 27:
			break  # esc to quit
	cv2.destroyAllWindows()
