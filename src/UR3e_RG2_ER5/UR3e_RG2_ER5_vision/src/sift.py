#!/usr/bin/env python3


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

def img_segmentation():
    rospy.loginfo("Hello from img_segmentation") 



class PubSub(object):
    # Class Varialbes 
    


    def __init__(self,sub_topic,sub_type):
        #Instance Varialbes  
        self.sub_topic = sub_topic
        self.sub_type = sub_type
        # self.pub_topic = pub_topic
        # self.pub_type = pub_type

        self.value = 7
        self.frame = None


        # Initlize the node 
        rospy.init_node('sift')
        self.br = CvBridge()
        # self.pub = rospy.Publisher(self.pub_topic, self.pub_type, queue_size=10)
        rospy.Subscriber(self.sub_topic, self.sub_type, self.callback)



    # Subscriber 
    def callback(self, data):
        
        rospy.loginfo("receiving video frame in CB")

        current_frame = self.br.imgmsg_to_cv2(data)

        sift = cv2.SIFT_create()
        kp = sift.detect(current_frame,None)  # function that find keypoints in the image
        img_kp=cv2.drawKeypoints(current_frame,kp,None) # Draw small circles o nthe location of keypoints

        cv2.imshow("current_frame", img_kp)
        cv2.waitKey(1)        



    # Publisher 
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #Publishingto topic 
            self.pub.publish(self.value)
            r.sleep()





if __name__ == '__main__':

    


    echo = PubSub('/ROI', Image)
    # echo.run()
    rospy.spin()