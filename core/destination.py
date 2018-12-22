import cv2
import numpy as np

import color
import detect

width, height = 480, 320

CAP = cv2.VideoCapture(1)

# GUI
des = np.array([0,0])
img_copy = CAP.read()[1]
def draw_point(event, x, y, flags, param):
    global des, img_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        des[0]=x
        des[1]=y
        print((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img_copy, (x, y), 3, (0, 0, 255), -1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_point)



print("click destination: (s, e)")
while True:
    _, img = CAP.read()

    corners = detect.detect_corners(img)
    if corners is None:
        continue

    corners = detect.sorted_corners(corners)

    pts1 = np.float32(corners)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, M, (width, height))
    
    cv2.imshow('image', img)
    
    if cv2.waitKey(1) == ord('s'):
        print('s')
        break
img_copy = img.copy()
while True:
    cv2.imshow('image', img_copy)
    if cv2.waitKey(1) == ord('e'):
        print('e')
        break

CAP.release()
cv2.destroyAllWindows()