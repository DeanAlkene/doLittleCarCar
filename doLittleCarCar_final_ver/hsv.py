import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H','image',0,180,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    # get current positions of four trackbars
    H = cv2.getTrackbarPos('H','image')
    S = cv2.getTrackbarPos('S','image')
    V = cv2.getTrackbarPos('V','image')

    img[:] = [H,S,V]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

cv2.destroyAllWindows()