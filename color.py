"""
通过手动选定蓝、绿、红（b，g，r）区域 <- 改了噢，头蓝尾绿噢
来获得更合适的颜色信息
及识别各个颜色的函数
"""

import cv2
import numpy as np
import perspective

CAP = cv2.VideoCapture(1)  # 开摄像头看东西噢

# 做GUI你需要全局变量和事件绑定函数噢
drawing = False
ix, iy = -1, -1
b_g_r = [(255, 225, 0), (0, 255, 0), (0, 0, 255)]
color = 0
region = [[], []]
img_copy = CAP.read()[1]


def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, b_g_r, color, region, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        region[color].append((x, y))
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), b_g_r[color], 2)

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix, iy), (x, y), b_g_r[color], 2)
        drawing = False
        region[color].append((x, y))
        color += 1


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)
# 上边就是框头尾的GUI了噢


# 执行了噢
print("Please label head and tail (enter 's' to start, 'e' to end): ")
while True:
    _, img = CAP.read()
    img = perspective.perspective(img)
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
# 执行完了噢

# 知道头尾框框位置了噢
blue, green = [img[
               region[i][0][1] + 1:region[i][1][1] - 1,
               region[i][0][0] + 1:region[i][1][0] - 1
               ] for i in range(2)]

# 计算当前情况下所需的bgr颜色在hsv色彩空间的取值范围
b_hsv = cv2.cvtColor(blue, cv2.COLOR_RGB2HSV)
g_hsv = cv2.cvtColor(green, cv2.COLOR_RGB2HSV)
b_mean_hsv, g_mean_hsv = [clr.mean(axis=0).mean(axis=0) for clr in (b_hsv, g_hsv)]
print("hsv of head and tail:", '\n', b_mean_hsv, '\n', g_mean_hsv)

offset = 10  # 名为offset实际应该是variance噢
lower_g, upper_g = g_mean_hsv - offset, g_mean_hsv + offset
lower_b, upper_b = b_mean_hsv - 2*offset, b_mean_hsv + 2*offset
lower_b[1] = lower_g[1] = 128
lower_b[2] = lower_g[2] = 46
upper_b[1] = upper_g[1] = upper_b[2] = upper_g[2] = 255


# 最终得到头尾颜色识别函数了噢
def Thresh_green(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_g, upper_g)
    return mask


def Thresh_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_b, upper_b)
    return mask
