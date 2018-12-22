import cv2
import numpy as np


# big = np.zeros((100,700,3),dtype=np.uint8)


# img = np.zeros((50,600,3),dtype=np.uint8)
# img.fill(255)


def padding(img,len):
    img_m, img_n = img.shape[0:2] # Amxn
    big = np.zeros((img_m+2*len,img_n+2*len,3),dtype=np.uint8)
    big.fill(225)
    big[2*len:img_m,2*len:img_n]=img[len:img_m-len,len:img_n-len]
    return big


# pad = padding(img,100)
# while 1:
#     cv2.imshow("pad",pad)
#     if cv2.waitKey(1)==ord('q'):
#         break