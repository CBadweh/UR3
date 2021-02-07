#!/usr/bin/env python3

#2ndst ed: Just subscribe from Topic with type = Image; and publish to topic with type = Image, then displace images 
    # implementing image segmenation 

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



    # def run(self):
    #     r = rospy.Rate(10)
    #     while not rospy.is_shutdown():
    #         #Publishingto topic 
    #         if self.image is not None:
    #             self.pub.publish(self.image)
    #         r.sleep()

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



def img_segmentation(clean_image, object_image):
    # ============================================================= 
    # Image Segmentation 
    #============================================================== 
    # rospy.loginfo("Hello from img_segmentation") 

    #==== convert the images to grayscale ==============
    grayA = cv2.cvtColor(clean_image, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(object_image, cv2.COLOR_BGR2GRAY)

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
    #   # compute the bounding box of the contour and then draw the
    #   # bounding box on both input images to represent where the two
    #   # images differ
    #   (x, y, w, h) = cv2.boundingRect(c)
    #   cv2.rectangle(default_view, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #   cv2.rectangle(Object_videw, (x, y), (x + w, y + h), (0, 0, 255), 2)

    ROI = cv2.bitwise_and(object_image,object_image,mask = thresh)
    ROICopy = ROI.copy()


    # === Diplaying =====
    # cv2.imshow("default_view", default_view)
    # cv2.imshow("Object_videw", object_image)
    # # cv2.imshow("RGB_image", RGB_image) # straming video 
    # cv2.imshow("Thresh", thresh)
    # cv2.imshow("ROI", ROI)
    return ROI
    #rospy.loginfo("  End of img_segmentation") 





class PubSub(object):
    # Class Varialbes 
    clean_image = cv2.imread('/home/cbadweh/UR3/default_view.jpg') 
    object_image = cv2.imread('/home/cbadweh/UR3/view_with_object.jpg')
    ROI = None
    imgMsg = None
    


    def __init__(self,sub_topic,sub_type,pub_topic,pub_type):
        #Instance Varialbes  
        self.sub_topic = sub_topic
        self.sub_type = sub_type
        self.pub_topic = pub_topic
        self.pub_type = pub_type
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
        current_frame = self.br.imgmsg_to_cv2(data,"bgr8")

        #== Image Segmentation 
        self.ROI = img_segmentation(self.clean_image,self.object_image)


        self.imgMsg = self.br.cv2_to_imgmsg(self.ROI)



        #==== Display =============================
        # cv2.imshow("clean_image", self.clean_image)
        # cv2.imshow("object_image", self.object_image)
        # cv2.imshow("ROI", self.ROI)
        # # cv2.imshow("current_frame", self.current_frame)
        # cv2.waitKey(1)        



    # Publisher 
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #Publishingto topic 
            # self.pub.publish(self.imgMsg)
            if self.ROI is not None:
                self.pub.publish(self.imgMsg)
            r.sleep()





if __name__ == '__main__':

    

    
    echo = PubSub('/camera/color/image_raw', Image, '/out_value', Image)
    echo.run()

