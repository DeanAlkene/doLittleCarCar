import cv2
import numpy as np

# red
lower_red1 = np.array([0, 128, 46])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([156, 128, 46])
upper_red2 = np.array([180, 255, 255])
def Thresh_red(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    return cv2.bitwise_or(mask1, mask2)


# green
lower_green = np.array([45,43,46])
upper_green = np.array([75,255,255])
def Thresh_green(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    return mask


# blue
lower_blue = np.array([110, 43, 46])
upper_blue = np.array([120, 255, 255])
def Thresh_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask


# yellow
lower_yellow = np.array([26,43,46])
upper_yellow = np.array([34,255,255])
def Thresh_yellow(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    return mask
