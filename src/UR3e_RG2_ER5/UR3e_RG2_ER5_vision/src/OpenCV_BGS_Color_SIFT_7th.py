#!/usr/bin/env python3

#
# 7th Subscribe to a /out_val from BackGround_Subtraciton_node
#       -Store SIFT's keypoint  and descriptors into the varialbe 'SIFT_msg'
#       -publish SIFT_msg
# Goal: Publish color info msg 

import rospy
import sys
import cv2
import cv2.xfeatures2d
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

from skimage.measure import compare_ssim
import argparse
import imutils
from std_msgs.msg import Int16, Float32
from UR3e_RG2_ER5_vision.msg import UR3CV, UR3CVKeypointsVector, UR3CVKeypoints, UR3Numpy
import copy
import numpy as np
from rospy.numpy_msg import numpy_msg 

#============================================================= 
# Detect color 
#==============================================================
def color_detection(ROI_image):
    # resources: https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
    # rospy.loginfo("Hello from color_detection") 


    imageFrame = ROI_image.copy()

    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

    # Color list 
    colorList = []

    # cv2.imshow("imageFrame", imageFrame) 
    # cv2.imshow("hsvFrame", hsvFrame) 

# DEFINE COLOR

    # Set range for red color and 
    # define mask 
    # red_lower = np.array([136, 87, 111], np.uint8) 
    # red_upper = np.array([180, 255, 255], np.uint8) 
    red_lower = np.array([0, 50, 120], np.uint8) 
    red_upper = np.array([10, 255, 255], np.uint8) 
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

    # Set range for yellow color and 
    # define mask 
    yellow_lower = np.array([22, 93, 0], np.uint8) 
    yellow_upper = np.array([45, 255, 255], np.uint8) 
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 
    
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernal = np.ones((5, 5), "uint8") 

# MASK COLOR
 
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

    # For yellow color 
    yellow_mask = cv2.dilate(yellow_mask, kernal) 
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame, 
                            mask = yellow_mask) 


    # cv2.imshow("green_mask", green_mask) 
    # cv2.imshow("res_red", res_red) 

# CREATE CONTOUR

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

            # rospy.loginfo("RED") 
            colorList.append("RED")

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

            # rospy.loginfo("GREEN") 
            colorList.append("Green")




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

            # rospy.loginfo("Blue") 
            colorList.append("Blue")



    # Creating contour to track yellow color 
    contours, hierarchy = cv2.findContours(yellow_mask, 
                                        cv2.RETR_TREE, 
                                        cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                    (x + w, y + h), 
                                    (255, 0, 0), 2) 
            
            cv2.putText(imageFrame, "Yellow Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 0, 0)) 
            colorList.append("Yellow")





    # # Program Termination 
    # rospy.loginfo(colorList) 
    # cv2.imshow("imageFrame", imageFrame) 
    # cv2.imshow("hsvFrame", hsvFrame) 
    # cv2.imshow("green_mask", green_mask) 
    return imageFrame, colorList



# making_msg() return sift_msg, which ros will publish for SIFT info 

def making_msg(kp, des, img_kp):
    # rospy.loginfo("making_msg")     # Debug
    # cv2.imshow("img_kp", img_kp)    # Debug

    #  init ros custom message
    sift_msg = UR3CVKeypointsVector() 
    Keypoint = UR3CVKeypoints()
    Descriptor = UR3Numpy()

    

    #====UPDATING 'sift_msg' for each point===================
    sift_msg.Keypoint_Length = len(kp)
    # for i in range(len(interested_kp)):
    for i in range(4):
        #__Appending each new Keypoint and Descriptor to the SIFT_msg to be publish________

        # updating each Keypoint info
        Keypoint.angle = kp[i].angle
        Keypoint.class_id = kp[i].class_id
        Keypoint.octave = kp[i].octave
        Keypoint.pt = str(kp[i].pt)
        Keypoint.response = kp[i].response
        Keypoint.size = kp[i].size
        sift_msg.Kp.append(copy.deepcopy((Keypoint)))   # appending each keypoint to SIFT_msg to be publish 

        # updating each Descriptor
        Descriptor.Descriptor = des[i]
        sift_msg.Des.append(copy.deepcopy((Descriptor))) # appending each Descriptor to SIFT_msg to be publish 

        rospy.loginfo("Kp %s", Keypoint)
        rospy.loginfo("Des %s" ,Descriptor)

    return sift_msg
    



class Echo(object):

    def __init__(self):

        # initilization 
        rospy.init_node('Color_SIFT_node')
        self.br = CvBridge()
        self.once_flag = 0  # still frame

        # Init SIFT Stuff
        self.sift = cv2.SIFT_create()
        

        # subscribing and publishing
        self.SIFT_msg = UR3CVKeypointsVector()
        self.pub_SIFT = rospy.Publisher('/SIFT',numpy_msg(UR3CVKeypointsVector), queue_size=10)
        rospy.Subscriber('/out_value', Image, self.update_value)


    def update_value(self, data):
        # rospy.loginfo("receiving video frame in CallBack")
        
        # ====== Pre Processing Image ==============

        # Filtering/Cleaning data
        current_frame = self.br.imgmsg_to_cv2(data)
        self.frame = current_frame
        # cv2.imshow("current_frame", current_frame) # Debug

        # _Resize_image__ - To only focus on the platform 
        upper_left = (215,300)
        bottom_right =(430, 470)
        y = bottom_right[1] - upper_left [1]
        x = bottom_right[0] - upper_left[0]
        # roi_img = roi_frame[upper_left[1]:(upper_left[1]+y), upper_left[0]:(upper_left[0]+x)]        
        cropped_frame= self.frame[upper_left[1]:(upper_left[1]+y), upper_left[0]:(upper_left[0]+x)]

        # ======= PROCESSING IMAGE ==================

        # Detecting color
        Detected_Color, ColorList = color_detection(cropped_frame)
        # Performing SIFT
        kp, des = self.sift.detectAndCompute(cropped_frame,None) # find Keypoints in the image, return list dataType
        img_kp=cv2.drawKeypoints(cropped_frame,kp,None) # Draw Keypoints on images




        # ======== CREATING ROS MSG ===================
        # Only evaluate a single frame by using self.once_flag
        if self.once_flag == 0: 
            interested_kp = kp
            interested_des = des
            interested_img_kp = img_kp
            # Creating SIFT_msg that will be publish
            self.SIFT_msg = making_msg(interested_kp, interested_des, interested_img_kp) 
            self.once_flag = 1
            


        # cv2.imshow("Detected_Color", Detected_Color)
        cv2.waitKey(1)


    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub_SIFT.publish(self.SIFT_msg)
            r.sleep()

if __name__ == '__main__':


    echo = Echo()
    echo.run()