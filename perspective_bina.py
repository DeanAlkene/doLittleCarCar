# -*- coding: utf-8 -*-
import numpy as np
import cv2
from imutils import resize
import matplotlib.pyplot as plt


def Perspective_bina(address, matrixA, matrixB):
    img = cv2.imread(address)
    rows, cols, ch = img.shape

    pts1 = np.float32(matrixA)
    pts2 = np.float32(matrixB)
    M = cv2.getPerspectiveTransform(pts1, pts2)

    img = cv2.warpPerspective(img, M, (300, 300))
    img = cv2.GaussianBlur(img, (3, 3), 3)
    img = resize(img, width=700)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 199, 11)

    th = cv2.bitwise_not(th)

    kernel = np.array([[0, 1, 1],
                       [0, 1, 0],
                       [1, 1, 0]], dtype='uint8')

    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    return th


pts1 = np.float32([[130, 20], [335, 28], [18, 230], [430, 230]])
pts2 = np.float32([[50, 0], [250, 0], [0, 300], [300, 300]])

img = Perspective_bina(
    'C:/Users/k1017/Desktop/block1/some/timg.jpg', pts1, pts2)
C_A = img[[0, 1, 2]]
C_A = C_A[:, [1, 2, 3]]
print(C_A)
for i in range(700):
    for j in range(700):
        print(img[i][j], end="")
    print('\n')
cv2.imshow('mask', img)
cv2.waitKey(0)
'''
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[50,0],[250,0],[0,300],[300,300]])

dst=Perspective("C:/Users/k1017/Desktop/block1/some/IMG_2993.JPG",pts1,pts2)
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''
