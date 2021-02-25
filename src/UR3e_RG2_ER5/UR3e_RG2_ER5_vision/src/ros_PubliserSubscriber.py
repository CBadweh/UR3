#!/usr/bin/env python3

#1st ed: Just subscribe and publish, then displace images 

#=======================================================================
# Template from Wiki 
#=======================================================================
#= Template of PublisherSubscribe node
#= Resource: https://answers.ros.org/question/62327/how-to-create-a-combining-subscriber-and-publisher-node-in-python/
#=
#= import rospy
#= from std_msgs.msg import Int32
#=
#= class Echo(object):
#=     def __init__(self):
#=         self.value = 0
#=
#=         rospy.init_node('echoer')
#=
#=         self.pub = rospy.Publisher('/out_value', Int32, latch=True)
#=         rospy.Subscriber('/in_value', Int32, self.update_value)
#=
#=     def update_value(self, msg):
#=         self.value = msg.data
#=
#=     def run(self):
#=         r = rospy.Rate(10)
#=         while not rospy.is_shutdown():
#=             self.pub.publish(self.value)
#=             r.sleep()
#
#  ||===========================================================================||




#=======================================================================
# Simple Node that publish and subscribe using OpenCv 
#=======================================================================

# from libries 

# class Echo(object):
#     def __init__(self):
#         self.value = 7


#         rospy.init_node('echoer')
#         self.br = CvBridge()

#         self.pub = rospy.Publisher('/out_value', Int32, queue_size=10)
#         rospy.Subscriber('/camera/color/image_raw', Image, self.update_value)

#     def update_value(self, data):
        
#         rospy.loginfo("receiving video frame in CB")
#         current_frame = self.br.imgmsg_to_cv2(data)
#         self.frame = current_frame
#         # rospy.loginfo(type(current_frame))
#         cv2.imshow("camera", self.frame)
#         cv2.waitKey(1)



#     def run(self):
#         r = rospy.Rate(10)
#         while not rospy.is_shutdown():
#             #Publishingto topic 
#             self.pub.publish(self.value)
#             r.sleep()

# if __name__ == '__main__':


#     echo = Echo()
#     echo.run()


# ||====================================================================================||


#=======================================================================
# The Real Code 
#=======================================================================


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


from std_msgs.msg import Int32




def img_segmentation():
    rospy.loginfo("Hello from img_segmentation") 



class PubSub(object):
    # Class Varialbes 
    


    def __init__(self,sub_topic,sub_type,pub_topic,pub_type):
        #Instance Varialbes  
        self.sub_topic = sub_topic
        self.sub_type = sub_type
        self.pub_topic = pub_topic
        self.pub_type = pub_type

        self.clean_image = cv2.imread('/home/cbadweh/UR3/default_view.jpg') 
        self.object_image = cv2.imread('/home/cbadweh/UR3/view_with_object.jpg')

        self.value = 7
        self.frame = None


        # Initlize the node 
        rospy.init_node('echoer')
        self.br = CvBridge()
        self.pub = rospy.Publisher(self.pub_topic, self.pub_type, queue_size=10)
        rospy.Subscriber(self.sub_topic, self.sub_type, self.callback)



    # Subscriber 
    def callback(self, data):
        
        rospy.loginfo("receiving video frame in CB")
        current_frame = self.br.imgmsg_to_cv2(data)
        img_segmentation()
 
        cv2.imshow("clean_image", self.clean_image)
        cv2.imshow("object_image", self.object_image)
        cv2.imshow("current_frame", current_frame)
        cv2.waitKey(1)        



    # Publisher 
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #Publishingto topic 
            self.pub.publish(self.value)
            r.sleep()





if __name__ == '__main__':

    


    echo = PubSub('/camera/color/image_raw', Image, '/out_value', Int32)
    echo.run()

