#!/usr/bin/env python3

# Simply stream video from Kinect 
# Covnert ROS Image to OpenCV Image 
# Apply Simple OpenCv Technique 
# Convert OpenCv Image to ROS Image 

import rospy
import sys
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


RGB_image = None


# 

def callbackRGB(data):

	# convert ROS image to OpenCV Image 
	global RGB_image
	bridge = CvBridge()
	# RGB_image = bridge.imgmsg_to_cv2(data, data.encoding) # color are mismatch 
	RGB_image = bridge.imgmsg_to_cv2(data, "bgr8") # with correct color 





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

		cv2.imshow("Color kinect", RGB_image)

		# press Esc key to exit out of the node 
		if cv2.waitKey(1) == 27:
			break 
	cv2.destoryAllWindows()
