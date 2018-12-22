import cv2
import numpy as np

def thin(img):
    img = cv2.GaussianBlur(img, (5, 5), 3)
    # img = resize(img, width=700)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 33,11)

    th = cv2.bitwise_not(th)

    kernel = np.array([[0, 1, 1],
                      [0, 1, 0],
                      [1, 1, 0]], dtype='uint8')

    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    return th

