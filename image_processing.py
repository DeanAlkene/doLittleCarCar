import cv2
import numpy as np
from thresh_color import *


def Gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def GaussianBlur(Gray):
    return cv2.GaussianBlur(Gray, (9, 9), 0)


# def Gradient(blurred):
#     gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
#     gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)
#     gradient = cv2.subtract(gradX, gradY)
#     return cv2.convertScaleAbs(gradient)


# def Thresh_and_blur(gradient):
#     blurred = cv2.GaussianBlur(gradient, (9, 9), 0)
#     (_, thresh) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
#     return thresh


###
# def image_morphology(thresh):
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
#
#     closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#     closed = cv2.erode(closed, None, iterations=4)
#     closed = cv2.dilate(closed, None, iterations=4)
#     return closed


def find_cnts(closed):
    (_, cnts, _) = cv2.findContours(closed.copy(),
                                    cv2.RETR_LIST,
                                    cv2.CHAIN_APPROX_SIMPLE)
    return cnts


def get_box(c):
    rect = cv2.minAreaRect(c)
    return np.int0(cv2.boxPoints(rect))


#########
def detect_corners(img):
    cnts_red = find_cnts(Thresh_red(img))
    try:
        sorted_cnts = sorted(cnts_red, key=cv2.contourArea, reverse=True)
        c_red = [sorted_cnts[i] for i in range(4)] # bug: sort_cnts[0:4]
    except:
        return None
    red_box = [get_box(c) for c in c_red]
    return [sum(r_b) // 4 for r_b in red_box]


def sorted_corners(corners):
    corners = sorted(corners, key=lambda c: sum(c))
    if corners[1][0] < corners[2][0]:
        corners[1], corners[2] = corners[2], corners[1]
    return corners


#########
def detect_car(img):
    cnts_green = find_cnts(Thresh_green(img))
    cnts_blue = find_cnts(Thresh_blue(img))

    try:
        c_green = sorted(cnts_green, key=cv2.contourArea, reverse=True)[0]
        c_blue = sorted(cnts_blue, key=cv2.contourArea, reverse=True)[0]
    except:
        return None

    box_green = get_box(c_green)
    box_blue = get_box(c_blue)

    head = sum(box_green) // 4
    tail = sum(box_blue) // 4

    return box_green, head, box_blue, tail


# def drawRotatedRect(rect, image, color, width):
#    box = cv2.boxPoints(rect)
#    x0, y0 = box[0]
#    for i in range(3):
#       x, y = box[i]
#       x1, y1 = box[i + 1]
#       cv2.line(image, (x, y), (x1, y1), color, width)
#       if i is 2:
#          cv2.line(image, (x1, y1), (x0, y0), color, width)
