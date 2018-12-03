import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("gb.png", 1)
size = img.shape
print(size)

# bgr
print(img[60][60], img[100][100])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv[60][60], hsv[100][100])

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
