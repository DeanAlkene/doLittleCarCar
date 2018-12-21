import cv2
import numpy as np
import serial
import serial.tools.list_ports

import color

import destination

import detect
import comBluetooth
import rotate


from padding import *
from thin import *
from park1_0 import *




cap = cv2.VideoCapture(1)  # 0 为电脑自带摄像头，1 为外接的摄像头，在 while 循环中使用 cv2.waitKey(100) 以放慢fps
port = serial.Serial("COM4", 9600, timeout = 1)
comBluetooth.comBlutooth('P', port)


width, height = 480, 320

oldOp = 'A'

while cap.isOpened():
    _, img = cap.read()
    cv2.imshow("origin",img)
    th_b = color.Thresh_blue(img)
    th_g = color.Thresh_green(img)
    th_r = color.Thresh_red(img)
    # cv2.imshow("th_b",th_b)
    # cv2.imshow("th_g", th_g)
    cv2.imshow("th_r", th_r)
    if cv2.waitKey(1)==ord('q'):
        comBluetooth.comBlutooth('S', port)
        break







    # 透视变换
    corners = detect.detect_corners(img)
    if corners is None:
        cv2.imshow("origin", img)
        # cv2.imshow("th_b", th_b)
        # cv2.imshow("th_g", th_g)
        cv2.imshow("th_r", th_r)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            comBluetooth.comBlutooth('S', port)
            break
        continue

    corners = detect.sorted_corners(corners)
    # print(corners)

    pts1 = np.float32(corners)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, M, (width, height))

    
    


    # img = padding(img,15)









    # detect小车车
    car = detect.detect_car(img)
    if car is None:
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            comBluetooth.comBlutooth('S', port)
            break
        continue

    _, head, _, tail = car

    cv2.circle(img, tuple(head), 3, (0, 255, 0), -1)
    cv2.circle(img, tuple(tail), 3, (255, 225, 0), -1)
    cv2.imshow("image", img)

    print(park(head, destination.des, 70))
    if park(head, destination.des, 70) == 'P':
        comBluetooth.comBlutooth('P', port)
        comBluetooth.comBlutooth('S', port)
        break

    





    th = thin(img)
    cv2.imshow('thin', th)



    try:
        op, l, m, r = rotate.rotate(th, 40,22, tail, head, oldOp)
        oldOp = op
        comBluetooth.comBlutooth(op, port)
        # print(op)


        lmr = img.copy()
        cv2.circle(lmr, tuple(l), 5, (127, 0, 127), -1)
        cv2.circle(lmr, tuple(m), 5, (0, 127, 127), -1)
        cv2.circle(lmr, tuple(r), 5, (127, 127, 0), -1)
        cv2.imshow("lmr", lmr)


        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(100) 以实现间隔100ms的拍摄
            comBluetooth.comBlutooth('S', port)
            break


    except:
        pass


port.close()
cap.release()
cv2.destroyAllWindows()
