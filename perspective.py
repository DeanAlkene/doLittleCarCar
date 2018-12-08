"""
一开始的时候手动点4个corners来进行透视变换，要按顺序点噢
顺序：1 2
     3 4 噢
"""
import cv2
import numpy as np

CAP = cv2.VideoCapture(1)  # 开摄像头看东西噢

# GUI
corners = []
img_copy = CAP.read()[1]


def draw_point(event, x, y, flags, param):
    global corners, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        corners.append((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img_copy, (x, y), 3, (0, 0, 255), -1)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_point)

print("Please click 4 corners (enter 's' to start, 'e' to end): ")

# 开始标定
while True:
    _, img = CAP.read()
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
cv2.destroyAllWindows()
# 标定完成

width, height = 640, 480


def perspective(img):
    pts1 = np.float32(corners)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(img, M, (width, height))


def show_info():
    print(corners)

    while 1:
        cv2.imshow("pers", perspective(img))
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    show_info()
