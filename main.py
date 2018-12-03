from image_processing import *

cap = cv2.VideoCapture(0) # waitKey(100) to set fps, set(cv2.CAP_PROP_FPS,xxx) is a fake in opencv3

while cap.isOpened():
    _, img = cap.read()

    corners = detect_corners(img)
    car = detect_car(img)
    # TODO: track = detect_track(img)

    if not corners or not car: # TODO: or not track
        cv2.imshow("draw_img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): # if not car wait(1) else wait(100)
            break
        continue

    # TODO: perspective transformation

    _, head, _, tail = car
    location = (head + tail) // 2

    cv2.circle(img, tuple(head), 3, (0, 255, 0), -1)
    cv2.circle(img, tuple(tail), 3, (255, 0, 0), -1)
    cv2.imshow("draw_img", img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
