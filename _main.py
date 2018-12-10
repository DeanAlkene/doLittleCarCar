import cv2
import numpy as np

"""
perspective 与 color 模块在 import 时执行了里边的东西噢
由于程序是从main开始执行的，在其他模块 import color 和 
perspective 时只能用他们里边的函数噢，不会再执行一次的噢
"""
import _perspective
import color
import detect

cap = cv2.VideoCapture(1)  # 0 为电脑自带摄像头，1 为外接的摄像头，在 while 循环中使用 cv2.waitKey(100) 以放慢fps

cv2.namedWindow("image")
cv2.namedWindow("hsv")
cv2.namedWindow("b")
cv2.namedWindow("g")
cv2.moveWindow("image", 500, 0)
cv2.moveWindow("hsv", 500, 400)
cv2.moveWindow("b", 1000, 0)
cv2.moveWindow("g", 1000, 400)

while cap.isOpened():
    _, img = cap.read()
    img = _perspective.perspective(img)  # 进行了透视变换噢
    # img = cv2.GaussianBlur(img, (9, 9), 0)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", hsv)

    # 看看蓝色绿色识别的怎么样噢
    b, g = color.Thresh_blue(img), color.Thresh_green(img)
    cv2.imshow("b", b)
    cv2.imshow("g", g)

    # detect小车车
    car = detect.detect_car(img)
    if not car:
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            break
        continue

    _, head, _, tail = car
    location = (head + tail) // 2

    cv2.circle(img, tuple(head), 3, (0, 255, 0), -1)
    cv2.circle(img, tuple(tail), 3, (255, 225, 0), -1)
    cv2.imshow("image", img)

    if cv2.waitKey(100) & 0xFF == ord('q'):  # wait(100) 以实现间隔100ms的拍摄
        break

cap.release()
cv2.destroyAllWindows()
