# -*- coding: utf-8 -*-
import cv2
from imutils import resize
import numpy as np

def Perspective(address,matrixA,matrixB):
    img = cv2.imread(address)
    rows,cols,ch = img.shape

    pts1 = np.float32(matrixA)
    pts2 = np.float32(matrixB)

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(img,M,(300,300))
    return dst

pts1 = np.float32([[130, 20], [335, 28], [18, 230], [430, 230]])
pts2 = np.float32([[50, 0], [250, 0], [0, 300], [300, 300]])

img=Perspective('C:/Users/k1017/Desktop/block1/some/timg.jpg',pts1,pts2)

img = cv2.GaussianBlur(img, (3, 3), 3)
img = resize(img, width=700)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY, 33,11)

th = cv2.bitwise_not(th)

kernel = np.array([[0, 1, 1],
                  [0, 1, 0],
                  [1, 1, 0]], dtype='uint8')

th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

cv2.imshow('mask', th)
cv2.waitKey(0)
