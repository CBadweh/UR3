#!/usr/bin/env python3

# Background subtraction node: 
# compareing 2 images and see the difference betwene them 
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
    (score, diff) = compare_ssim(grayA, grayB,gaussian_weights=True, full=True)
    diff = (diff * 255).astype("uint8")
    # print("SSIM: {}".format(score))

    # === Threshold the difference image=================
    # followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Take care of noise by filling holes 
    # https://learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
    im_floodfill = thresh.copy()
    h, w = thresh.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    im_out = thresh | im_floodfill_inv
    # cv2.imshow("Thresholded", thresh)
    # cv2.imshow("Floodfilled", im_floodfill)
    # cv2.imshow("Inverted", im_floodfill_inv)
    # cv2.imshow("Foreground", im_out)


    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # # loop over the contours, for draing bounding box 
    # for c in cnts:
    #   # compute the bounding box of the contour and then draw the
    #   # bounding box on both input images to represent where the two
    #   # images differ
    #   (x, y, w, h) = cv2.boundingRect(c)
    #   cv2.rectangle(default_view, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #   cv2.rectangle(Object_videw, (x, y), (x + w, y + h), (0, 0, 255), 2)

    ROI = cv2.bitwise_and(object_image,object_image,mask = im_out)



    # === Diplaying =====
    # # cv2.imshow("RGB_image", RGB_image) # straming video 
    # cv2.imshow("Thresh", thresh)
    # cv2.imshow("ROI", ROI)
    return ROI
    #rospy.loginfo("  End of img_segmentation") 





class PubSub(object):
    # Class Varialbes 
    # clean_image = cv2.imread('/home/cbadweh/Desktop/default_view.jpg')
    # object_image = cv2.imread('/home/cbadweh/Desktop/view_with_object.jpg')
    ROI = None
    imgMsg = None
    


    def __init__(self,sub_topic,sub_type,pub_topic,pub_type):
        #Instance Varialbes  
        self.sub_topic = sub_topic
        self.sub_type = sub_type
        self.pub_topic = pub_topic
        self.pub_type = pub_type
        self.frame = None
        self.clean_image = cv2.imread('/home/cbadweh/Desktop/default_view.jpg')
        self.object_image = cv2.imread('/home/cbadweh/Desktop/view_with_object.jpg')


        # Initlize the node 
        rospy.init_node('Background_Subtraction_node')
        self.br = CvBridge()
        self.fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
        self.pub = rospy.Publisher(self.pub_topic, self.pub_type, queue_size=10)
        rospy.Subscriber(self.sub_topic, self.sub_type, self.callback)



    # Subscriber 
    def callback(self, data):
        
        # rospy.loginfo("receiving video frame in CB")
        current_frame = self.br.imgmsg_to_cv2(data,"bgr8")
        self.frame = current_frame



        # Resize image - To only focus on the platform 
        upper_left = (215,300)
        bottom_right =(430, 470)
        y = bottom_right[1] - upper_left [1]
        x = bottom_right[0] - upper_left[0]
        # roi_img = roi_frame[upper_left[1]:(upper_left[1]+y), upper_left[0]:(upper_left[0]+x)]        
        cropped_frame= self.frame[upper_left[1]:(upper_left[1]+y), upper_left[0]:(upper_left[0]+x)]

        # ======= PROCESSING IMAGE ==================
        # Background subtraction processing
        fgmask1 = self.fgbg1.apply(current_frame) 
        # Extracing object of interested
        ROI_BG = cv2.bitwise_and(current_frame,current_frame,mask = fgmask1)


        #Image Segmentation 
        # self.ROI = img_segmentation(self.clean_image,self.object_image)   # find the difference between the twoinitilized images
        self.ROI = img_segmentation(self.clean_image,current_frame)		# find the diff between current image and the clean image



        # Store the img into ros msg to be publish
        self.imgMsg = self.br.cv2_to_imgmsg(self.ROI)

        #==== Display =============================
        cv2.imshow("ROI", self.ROI)
        cv2.imshow("ROI_BG", ROI_BG)


        cv2.waitKey(1)   





    # Publisher 
    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #Publishingto topic 
            # self.pub.publish(self.imgMsg) # option 1
            if self.ROI is not None:        # option 2
                self.pub.publish(self.imgMsg)
            r.sleep()





if __name__ == '__main__':

    

    
    echo = PubSub('/camera/color/image_raw', Image, '/out_value', Image)
    echo.run()

