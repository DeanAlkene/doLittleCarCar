import cv2
import numpy as np
import color
import detect

cap = cv2.VideoCapture(1)

while cap.isOpened():
    _, img = cap.read()

    car = detect.detect_car(img)
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

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
