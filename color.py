"""
通过手动选定蓝、绿、红（b，g，r）区域
来获得更合适的颜色信息
及识别各个颜色的函数
"""

import cv2
import numpy as np

CAP = cv2.VideoCapture(1)  # 0 为电脑自带摄像头，1 为外接的摄像头，在 while 循环中使用 cv2.waitKey(100) 以放慢fps


# 事件绑定，鼠标标定bgr区域所需要的全局变量及函数
drawing = False
ix, iy = -1, -1
b_g_r = [(255, 225, 0), (0, 255, 0), (0, 0, 255)]
color = 0
region = [[], [], []]


def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, b_g_r, color, region

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        region[color].append((x, y))
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            cv2.rectangle(img_copy, (ix, iy), (x, y), b_g_r[color], -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        region[color].append((x, y))
        color += 1


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

print("Please label blue, green and red (enter 's' to start, 'e' to end): ")

# 开始标定
while True:
    _, img = CAP.read()
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('s'):
        print('s')
        break
_, img = CAP.read()
img_copy = img.copy()
while (1):
    cv2.imshow('image', img_copy)
    if cv2.waitKey(1) == ord('e'):
        print('e')
        break
cv2.destroyAllWindows()
# 标定完成

blue, green, red = [img[region[i][0][1]:region[i][1][1], region[i][0][0]:region[i][1][0]] for i in range(3)]

# 确定一下标定的区域是否正确
while True:
    cv2.imshow("red", red)
    cv2.imshow("green", green)
    cv2.imshow("blue", blue)
    if cv2.waitKey(1) == ord('q'):
        break

CAP.release()
cv2.destroyAllWindows()

# 计算当前情况下所需的bgr颜色在hsv色彩空间的取值范围
b_hsv = cv2.cvtColor(blue, cv2.COLOR_RGB2HSV)
g_hsv = cv2.cvtColor(green, cv2.COLOR_RGB2HSV)
r_hsv = cv2.cvtColor(red, cv2.COLOR_RGB2HSV)
b_mean_hsv, g_mean_hsv, r_mean_hsv = [clr.mean(axis=0).mean(axis=0) for clr in (b_hsv, g_hsv, r_hsv)]
print("bgr_hsv:", b_mean_hsv, '\n', g_mean_hsv, '\n', r_mean_hsv)
# exit(0)

offset = 10
lower_r, upper_r = r_mean_hsv - offset, r_mean_hsv + offset
lower_g, upper_g = g_mean_hsv - offset, g_mean_hsv + offset
lower_b, upper_b = b_mean_hsv - offset, b_mean_hsv + offset
lower_b[1] = lower_g[1] = lower_r[1] = 43
lower_b[2] = lower_g[2] = lower_r[2] = 46
upper_b[1] = upper_g[1] = upper_r[1] = 255
upper_b[2] = upper_g[2] = upper_r[2] = 255


#最终得到3个用于识别颜色的函数
def Thresh_red(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_r, upper_r)
    return mask


def Thresh_green(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_g, upper_g)
    return mask


def Thresh_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_b, upper_b)
    return mask
