#!/usr/bin/env python3



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
from matplotlib import pyplot as plt

from std_msgs.msg import Int32


# ============================================================= 
# Image Segmentation 
#============================================================== 
def img_segmentation(clean_image, object_image):

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

# || End of img_segmentation -------------------------------------||



#============================================================= 
# Detect color 
#==============================================================
def color_detection(ROI_image):
    rospy.loginfo("Hello from color_detection") 


    imageFrame = ROI_image.copy()

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
    # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 
    return imageFrame





class PubSub(object):
    # Class Varialbes 
    clean_image = cv2.imread('/home/cbadweh/UR3/default_view.jpg') 
    object_image = cv2.imread('/home/cbadweh/UR3/view_with_object.jpg')
    ROI = None
    # color_detected = None

    


    def __init__(self,sub_topic,sub_type,pub_topic,pub_type):
        #Instance Varialbes  
        self.sub_topic = sub_topic
        self.sub_type = sub_type
        self.pub_topic = pub_topic
        self.pub_type = pub_type
        self.value = 7
        self.frame = None

        self.object_image_imgMsg = None
        self.ROI_imgMsg = None
        self.Color_detected_Msg = None

        # Initlize the node 
        rospy.init_node('OpenCV_BG_Subtraction')
        self.br = CvBridge()
        self.pub_Object_image = rospy.Publisher(self.pub_topic, self.pub_type, queue_size=10)
        # self.pub_ROI = rospy.Publisher('ROI', Image, queue_size=10)
        # self.pub_Color_detected = rospy.Publisher('Color_Detected', Image, queue_size = 10)

        rospy.Subscriber(self.sub_topic, self.sub_type, self.callback)



    # Subscriber 
    def callback(self, data):
        
        rospy.loginfo("receiving video frame in CB")
        current_frame = self.br.imgmsg_to_cv2(data,"bgr8")

        # rospy.loginfo("image size %s", current_frame.shape)

        roi_frame = current_frame.copy()


        # #==========DRAWING POINT TO FIND POINT OF INTEREST =================================================================================|
        # # ___Draw Polygon Shape_________                                                                                                    |
        # # https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/                                                                 |

        # pts = np.array([ [255, 360], [385, 360], [430, 470], [215, 470] ], np.int32) 
        # color = (0, 225, 0) # Green
        # thickness = 1
        # poly_frame =cv2.polylines(current_frame, [pts], True, color, thickness )

        # # ___Put Text_________
        # # https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
        # # rospy.loginfo("tuple  %s", tuple(pts[1]))

        # for i in range(len(pts)):
        #     poly_frame =cv2.putText(poly_frame, str(pts[i]), tuple(pts[i]), cv2.FONT_HERSHEY_SIMPLEX , .5, (255, 0, 100) , 1, cv2.LINE_AA)  | 
                                                                                                                                            # |
        # #==========DRAWING POINT TO FIND POINT OF INTEREST =================================================================================|

        # Bottom_bdry = np.array([ [215, 360], [430, 360], [430, 470], [215, 470] ], np.int32) 
        # # poly_frame =cv2.polylines(frame_roi, [Bottom_bdry], True, (0, 225, 0), 1 )
        # for i in range(len(Bottom_bdry)):
        #     poly_frame =cv2.putText(frame_roi, str(Bottom_bdry[i]), tuple(Bottom_bdry[i]), cv2.FONT_HERSHEY_SIMPLEX , .5, (255, 0, 100) , 1, cv2.LINE_AA)


        # Resize the image to only the roi 
        upper_left = (215,360)
        bottom_right =(430, 470)
        y = bottom_right[1] - upper_left [1]
        x = bottom_right[0] - upper_left[0]
        roi_img = roi_frame[upper_left[1]:(upper_left[1]+y), upper_left[0]:(upper_left[0]+x)]
        # cv2.rectangle(frame_roi,upper_left, bottom_right, (0,255,0), 2)



        # == convert cv2 to ros msg to be publish =========         
        # self.object_image_imgMsg = self.br.cv2_to_imgmsg(self.object_image)
        # self.ROI_imgMsg = self.br.cv2_to_imgmsg(self.ROI)
        # self.Color_detected_Msg = self.br.cv2_to_imgmsg(color_detected)

        # #==== Display =============================

        cv2.imshow("poly_frame", roi_frame)
        cv2.imshow("roi_img", roi_img)
        cv2.waitKey(1)      

    # || End of Subscriber's callback-------------------------------------------   




    # Publisher 
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #Publishingto topic 
            # self.pub.publish(self.imgMsg)
            if self.ROI is not None:
                self.pub_Object_image.publish(self.object_image_imgMsg,)
                self.pub_ROI.publish(self.ROI_imgMsg)
                self.pub_Color_detected.publish(self.Color_detected_Msg)
            r.sleep()





if __name__ == '__main__':


#          PubSub(sub_topic, sub_type, pub_topic, pub_type)    
    echo = PubSub('/camera/color/image_raw', Image, '/ROI_output', Image)
    echo.run()















#================================================================================================================
# RESOURCES USED 
#================================================================================================================
# subscribing to multiple topics: https://robotics.stackexchange.com/questions/6652/how-to-get-a-python-node-in-ros-subscribe-to-multiple-topics