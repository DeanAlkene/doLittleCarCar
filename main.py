import cv2
import numpy as np
from image_processing import *

cap = cv2.VideoCapture(0)  # waitKey(100) to set fps, set(cv2.CAP_PROP_FPS,xxx) is a fake in opencv3
width, height = 640, 480

while cap.isOpened():
    _, img = cap.read()

    # perspective transformation
    corners = detect_corners(img)
    if not corners:
        cv2.imshow("draw_img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # if not car wait(1) else wait(100)
            break
        continue

    pts1 = np.float32(sorted_corners(corners))
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, M, (width, height))

    # detect car
    car = detect_car(img)
    if not car:
        cv2.imshow("draw_img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    _, head, _, tail = car
    location = (head + tail) // 2

    cv2.circle(img, tuple(head), 3, (0, 255, 0), -1)
    cv2.circle(img, tuple(tail), 3, (255, 0, 0), -1)
    cv2.imshow("draw_img", img)

    # TODO: track = detect_track(img)


    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
