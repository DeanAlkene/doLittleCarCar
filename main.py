import cv2
import numpy as np
from skeleton import *
from perspective import *

pts1 = np.float32([[130, 20], [335, 28], [18, 230], [430, 230]])
pts2 = np.float32([[50, 0], [250, 0], [0, 300], [300, 300]])
origin=get_origin('C:/Users/k1017/Desktop/block1/some/timg.jpg')
img= Perspective('C:/Users/k1017/Desktop/block1/some/timg.jpg',pts1,pts2)
img= Skeleton(img)
img = resize(img, 700)
cv2.imshow('mask', img)
cv2.imshow('origin', origin)
cv2.waitKey(0)
cv2.destroyAllWindows()
