#!/usr/bin/env python3

# Simply stream video from Kinect 
# Covnert ROS Image to OpenCV Image 
# Apply Simple OpenCv Technique 
# Convert OpenCv Image to ROS Image 

# tutorial link: 
#		youtube sentdex Color Filter 

import rospy
import sys
import cv2
import cv2.xfeatures2d
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

import numpy as np


RGB_image = None
# 

def callbackRGB(data):

	# convert ROS image to OpenCV Image 
	global RGB_image
	bridge = CvBridge()
	RGB_image = bridge.imgmsg_to_cv2(data, "bgr8")





if __name__ == '__main__':

	rospy.init_node('background_subtract')
	rospy.Subscriber('/camera/color/image_raw', Image, callbackRGB)

	# wait for image to arrive to node
	rate = 100
	r = rospy.Rate(rate)
	while RGB_image is None:
		print("Waiting for color image")
		r.sleep()


	# start streaming 
	while True:
		#------Oiginal Image Before any modification----------
		cv2.imshow("RGB_image", RGB_image)

		#------Color filter for blue------------- 
		hsv = cv2.cvtColor(RGB_image, cv2.COLOR_BGR2HSV)    # Convert to hsv
		lower_blue = np.array([75,61,51])					# Upper bound for the color to mask 
		upper_blue = np.array([225,225,225])
		mask = cv2.inRange(hsv,lower_blue,upper_blue)		# creat a mask for for blue color 
		blue = cv2.bitwise_and(RGB_image,RGB_image, mask = mask)
		cv2.imshow("Blue", blue)


		#------Apply Gussian Blue-----------------
		gaussian_blue = cv2.GaussianBlur(blue, (15,15),0)
		cv2.imshow("gaussian_blue", gaussian_blue)

		
		#----Canny Edge detection-----------------
		Canny = cv2.Canny(RGB_image, 100,200)
		cv2.imshow("Canny Edge Detector", Canny)

		
		
		

		# press Esc key to exit out of the node 
		if cv2.waitKey(1) == 27:
			break 
	cv2.destoryAllWindows()
