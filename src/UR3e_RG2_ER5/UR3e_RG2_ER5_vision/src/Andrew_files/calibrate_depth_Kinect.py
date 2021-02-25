from collections import Counter
import rospy
import time
from sensor_msgs.msg import Image
import cv2
import numpy as np
import sys
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
Depth_image = None
RGB_image = None

def funcBrightContrast(bright=0):
    bright = cv2.getTrackbarPos('bright', 'Life2Coding')
    contrast = cv2.getTrackbarPos('contrast', 'Life2Coding')

    effect = apply_brightness_contrast(img,bright,contrast)
    cv2.imshow('Effect', effect)

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    contrast = map(contrast, 0, 254, -127, 127)
    buf = input_img.copy()

    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    #cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def callbackDepth(data):
    global Depth_image
    Depth_image = bridge.imgmsg_to_cv2(data, data.encoding)

def callbackRGB(data):
    global RGB_image
    RGB_image = bridge.imgmsg_to_cv2(data, data.encoding)

# print(cv_image)
# print(image.encoding)
# (rows, cols, channels) = cv_image.shape
# new_image = cv_image
# return cv_image
# cv2.waitKey(3    while(1):)
#cv2.meanStdDev

if __name__ == '__main__':

    rospy.init_node('camera_node')
    #rospy.Subscriber('/kinect2/hd/image_color', Image, callbackRGB)
    rospy.Subscriber('/kinect2/qhd/image_color', Image, callbackRGB)
    rospy.Subscriber('/kinect2/sd/image_depth', Image, callbackDepth,queue_size=1)
    #rospy.Subscriber('/kinect2/qhd/image_depth_rect', Image, callbackDepth)
    rate = 100
    bright = 255
    contrast = 127
    cv2.namedWindow('Life2Coding',1)
    cv2.createTrackbar('bright', 'Life2Coding', bright, 2*255, funcBrightContrast)
    cv2.createTrackbar('contrast', 'Life2Coding', contrast, 3*127, funcBrightContrast)

    r = rospy.Rate(rate)
    while RGB_image is None:
        r.sleep()
    while Depth_image is None:
        r.sleep()


    #first_frame = cv2.imread('background_front.jpg',0)
    while True:
        img = Depth_image.copy()
        funcBrightContrast(0)
        cv2.imshow("Color Kinect", RGB_image)
        cv2.imshow("Depth Kinect", Depth_image)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()
