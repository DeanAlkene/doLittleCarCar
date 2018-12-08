import cv2
import numpy as np
import color
import detect

cap = cv2.VideoCapture(1)
width, height = 640, 480

while cap.isOpened():
    _, img = cap.read()

    # 透视变换
    corners = detect.detect_corners(img)
    if not corners:
        cv2.imshow("draw_img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    pts1 = np.float32(detect.sorted_corners(corners))
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, M, (width, height))


    # detect小车车
    car = detect.detect_car(img)
    if not car:
        cv2.imshow("draw_img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            break
        continue

    _, head, _, tail = car
    location = (head + tail) // 2

    cv2.circle(img, tuple(head), 3, (0, 255, 0), -1)
    cv2.circle(img, tuple(tail), 3, (255, 0, 0), -1)
    cv2.imshow("draw_img", img)

    if cv2.waitKey(100) & 0xFF == ord('q'): # wait(100) 以实现间隔100ms的拍摄
        break

cap.release()
cv2.destroyAllWindows()
