#!/usr/bin/env python3


"""
This program takes the background subtracted image and runs a blob detection on it.
It then finds the minimum sphere for the blob and relates it into 3D space as a marker.

"""

from collections import Counter
import rospy
import time
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import time

import cv2
import numpy as np
import sys
import math
import tf

import random as rng


from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
Depth_image = None
Bksub_image = None
RGB_image = None
Points = None
flag = None
cheight = None
cwidth = None
pName = "image_segmentation: "

#-- Converts ROS image into openc image	
def callbackPoints(data):
	global Points
	Points = data

#-- Converts ROS image into openc image	
def callbackDepth(data):
	global Depth_image
	global flag
	Depth_image2 = np.asarray(bridge.imgmsg_to_cv2(data, 'passthrough'))
	Depth_image = np.nan_to_num(Depth_image2)

#-- Converts ROS image into openc image	
def callbackBKSub(data):
	global Depth_image
	global Bksub_image
	global flag
	Bksub_image = np.asarray(bridge.imgmsg_to_cv2(data, 'passthrough'))
	flag    =   1

#-- Converts ROS image into openc image	
def callbackRGB(data):
	global RGB_image
	RGB_image = bridge.imgmsg_to_cv2(data, data.encoding)

#-- Converts pixels info into depth info using kinect intrinsics
def getXYZfromUVD(x1,y1,depth):
	fx = 554.254691191187
	fy = 554.254691191187
	cx = 320.5
	cy = 240.5
		
	y = (y1 - cy) * depth / fy
	x = (x1 - cx) * depth / fx
	return x,y,depth


if __name__ == '__main__':

	rospy.init_node('segmentation')
	rospy.Subscriber('/camera/color/image_raw', Image, callbackRGB)
	rospy.Subscriber('/bksub_image', Image, callbackBKSub)
	rospy.Subscriber('/camera/depth/image_raw', Image, callbackDepth)
	rospy.Subscriber('/camera/depth/points', PointCloud2, callbackPoints)
	
	listener = tf.TransformListener()	
	#rate = rospy.Rate(10.0)
	
	#while not rospy.is_shutdown():
		#try:
		#(trans,rot) = listener.lookupTransform('base_link', 'camera_link', rospy.Time(0))

		#except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		#	continue
		#print("Trying to get coord frame")
	#PubDepthImg = rospy.Publisher('depth_image_norm', String)
	PubBksubImg = rospy.Publisher('bksub_image', Image, queue_size=10)
	
	rate = 100
	r = rospy.Rate(rate)
	while Depth_image is None:
		print(pName + "Waiting for depth image")
		r.sleep()
	while RGB_image is None:
		print(pName + "Waiting for color image")
		r.sleep()

	print(pName + "Found it!")
	#print(pName + str(trans))
	color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
	while True:
		#print(Points)
		cv2.imshow(pName + "Color Kinect", RGB_image)
		cv2.imshow(pName + "Depth Kinect", Depth_image)

		ret,thresh = cv2.threshold(Bksub_image,127,255,0)
		#-- find contours in the binary image
		# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		
		centers = [None]*len(contours)
		radius = [None]*len(contours)
		mu = [None]*len(contours)
		mc = [None]*len(contours)
		max_depth = [0.0]*len(contours)
		min_depth = [1000.0]*len(contours)
		mid_depth = [0.0]*len(contours)
		points3d = [None]*len(contours)
		for i in range(len(contours)):
			#print("The min_depth is " + str(min_depth[0]))
			mu[i] = cv2.moments(contours[i])
			#-- Get the mass centers
			centers[i], radius[i] = cv2.minEnclosingCircle(contours[i])
			flag_1 = 0
			for j in range(len(contours[i])):
				try:
					x = Depth_image[contours[i][j][0][0],contours[i][j][0][1]]
					flag_1 = 1
					#print("J is"+ str(j) + "x is:" + str(x))
				except:
					flag_1 = 0
					None
	
				if x <= min_depth[i] and not 0:
					min_depth[i] = x
				if x >= max_depth[i] and not 0:
					max_depth[i] = x

			mid_depth[i] = ((max_depth[i] - min_depth[i])/2.0)

			mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5)) #-- add 1e-5 to avoid division by zero
			
			if(flag):
				points3d[i] = list(getXYZfromUVD(int(mc[i][0]),int(mc[i][1]),mid_depth[i]))
			
				points3d[i][0] = .001 - points3d[i][0]
				points3d[i][1] = 1.0 - points3d[i][1]
				points3d[i][2] = -.45 - points3d[i][2]
				print(points3d[i])

				cv2.circle(RGB_image, (int(mc[i][0]), int(mc[i][1])), int(radius[i]), color, 2)
				cv2.drawContours(RGB_image, contours, i, color, 2)
				cv2.circle(RGB_image, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)

		#depth_message = bridge.cv2_to_imgmsg(Depth_image, encoding="passthrough")
		try:		
			None
		except:
			#print("Not Published")
			None
		
		if cv2.waitKey(1) == 27:
			break  # esc to quit
	cv2.destroyAllWindows()
