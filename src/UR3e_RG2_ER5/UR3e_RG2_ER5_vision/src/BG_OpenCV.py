#!/usr/bin/env python3

# Background subtraction node: 
# compareing 2 images and see the difference betwene them 
# 
# Progress: 
	# -capture image once every second
	# -Only publish image that's stable 
# 

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
from UR3e_RG2_ER5_vision.msg import UR3CV, UR3CVKeypointsVector, UR3CVKeypoints, UR3Numpy, UR3Color
import copy
import numpy as np
from rospy.numpy_msg import numpy_msg 

from std_msgs.msg import Int32, Int16, Float32
from function import color_detection, image_stats, making_msg, cropped_image,LAB_color_stddev_mean,making_Color_msg, img_segmentation




def Stability(ROI_BG,black_img):
	PubSub.i += 1
	if(PubSub.i == 5):
		PubSub.i =0
		if PubSub.pervious_Frame is not None:
			# Stability_score = 1 if the object is stable
			PubSub.Stability_score, compared_img =img_segmentation(PubSub.pervious_Frame,ROI_BG)
			# rospy.loginfo("Object Stability : %s", PubSub.Stability_score)

			PubSub.empty_compared_score, empty_compared_img =img_segmentation(black_img,ROI_BG)
			# rospy.loginfo("empty_compared_score : %s", PubSub.empty_compared_score)


			if PubSub.empty_compared_score > 0.99:
				# rospy.loginfo("Empty")
				PubSub.already_pub = False
			else: 
				if PubSub.already_pub is False:
					# if stablity > 0.99, then pub and set pub_fleg to flase 
					if PubSub.Stability_score > 0.99:
						# self.imgMsg = self.br.cv2_to_imgmsg(self.ROI)
						PubSub.already_pub = True
						rospy.loginfo("Publish")
						return ROI_BG

		PubSub.pervious_Frame = ROI_BG
		# PubSub.i =0
		# cv2.imshow("Object Stability", PubSub.pervious_Frame)
	# rospy.loginfo("i : %s", PubSub.i)





class PubSub(object):
	# Class Varialbes 
	# clean_image = cv2.imread('/home/cbadweh/Desktop/default_view.jpg')
	# object_image = cv2.imread('/home/cbadweh/Desktop/view_with_object.jpg')
	ROI = None
	# imgMsg = None
	pervious_Frame = None
	Stability_score = None
	empty_compared_score = None
	empty = True
	i = 0
	already_pub = False


	def __init__(self,sub_topic,sub_type,pub_topic,pub_type):
		#Instance Varialbes  
		self.sub_topic = sub_topic
		self.sub_type = sub_type
		self.pub_topic = pub_topic
		self.pub_type = pub_type
		self.frame = None
		# self.pervious_Frame = None
		self.new_obj = 0
		self.i = 0
		self.clean_image = cv2.imread('/home/cbadweh/Desktop/default_view.jpg')
		self.object_image = cv2.imread('/home/cbadweh/Desktop/view_with_object.jpg')
		self.imgMsg = None


		# Initlize the node 
		rospy.init_node('Background_Subtraction_node')
		self.br = CvBridge()
		self.sift = cv2.SIFT_create()
		self.SIFT_msg = UR3CVKeypointsVector()
		self.COLOR_msg =UR3Color()
		self.fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
		self.pub_SIFT = rospy.Publisher('/SIFT',numpy_msg(UR3CVKeypointsVector), queue_size=10)
		self.pub_Color = rospy.Publisher('/Color',UR3Color, queue_size=10)

		# self.pub = rospy.Publisher(self.pub_topic, self.pub_type, queue_size=10)
		# self.new_obj_pub = rospy.Publisher('/Bg_Sub_New_Obj', Int32, queue_size=10)
		rospy.Subscriber(self.sub_topic, self.sub_type, self.callback)

	# Subscriber 
	def callback(self, data):
		
		# rospy.loginfo("receiving video frame in CB")
		current_frame = self.br.imgmsg_to_cv2(data,"bgr8")
		self.frame = current_frame

		# rospy.loginfo("size %s", current_frame.shape)
		# cv2.imshow("black_img", black_img)
		# empty_compared_score, empty_compared_img =img_segmentation(black_img,ROI_BG)

		# ======= PROCESSING IMAGE ==================
		# Background subtraction processing
		fgmask1 = self.fgbg1.apply(current_frame) 
		# Extracing object of interested
		ROI_BG = cv2.bitwise_and(current_frame,current_frame,mask = fgmask1)
		black_img = np.zeros(ROI_BG.shape,dtype='uint8')
		cropped_black_img = cropped_image(black_img)
		cropped_ROI_BG = cropped_image(ROI_BG)

		single_frame = Stability(cropped_ROI_BG,cropped_black_img)
		if single_frame is not None:
			# =========== Starting Image Process =======================
			cv2.imshow("single_frame", single_frame)
			rospy.loginfo("Publish msg")

			lMean, lStd, aMean, aStd, bMean, bStd = LAB_color_stddev_mean(single_frame)
			kp, des = self.sift.detectAndCompute(single_frame,None)
			img_kp=cv2.drawKeypoints(single_frame,kp,None) # Draw Keypoints on images
			cv2.imshow("img_kp_main", img_kp)

			self.SIFT_msg = making_msg(kp,des, img_kp)
			self.COLOR_msg = making_Color_msg(lMean, lStd, aMean, aStd, bMean, bStd)
			rospy.loginfo("SIFT_msg %s", self.SIFT_msg)
			rospy.loginfo("COLOR_msg %s", self.COLOR_msg)



		# =====Image Segmentation========= 
		# self.ROI = img_segmentation(self.clean_image,self.object_image)   # find the difference between the twoinitilized images
		_, self.ROI = img_segmentation(self.clean_image,current_frame)		# find the diff between current image and the clean image

		#==== Display =============================
		# cv2.imshow("ROI", self.ROI)
		# cv2.imshow("ROI_BG", cropped_ROI_BG)
		cv2.waitKey(1)   


	# Publisher 
	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			#Publishingto topic 
			# self.pub.publish(self.imgMsg) # option 1
			if self.SIFT_msg is not None:        # option 2
				self.pub_SIFT.publish(self.SIFT_msg)
				self.pub_Color.publish(self.COLOR_msg)
			r.sleep()





if __name__ == '__main__':

	

	
	echo = PubSub('/camera/color/image_raw', Image, '/out_value', Image)
	echo.run()

