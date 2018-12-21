# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt


def Perspective(address, matrixA, matrixB):
    img = cv2.imread(address)
    rows, cols, ch = img.shape

    pts1 = np.float32(matrixA)
    pts2 = np.float32(matrixB)

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (300, 300))
    return dst


'''
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[50,0],[250,0],[0,300],[300,300]])

dst=Perspective("C:/Users/k1017/Desktop/block1/some/IMG_2993.JPG",pts1,pts2)
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''
