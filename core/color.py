"""
通过手动选定蓝、绿、红（b，g，r）区域
来获得更合适的颜色信息
及识别各个颜色的函数
"""

import cv2
import numpy as np

# import _perspective

CAP = cv2.VideoCapture(1)  # 开摄像头看东西噢

# 做GUI你需要全局变量和事件绑定函数噢
drawing = False
ix, iy = -1, -1
b_g_r = [(255, 225, 0), (0, 255, 0), (0, 0, 255)]
color = 0
region = [[], [], []]
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
            cv2.rectangle(img_copy, (ix, iy), (x, y), b_g_r[color], 1)

    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix, iy), (x, y), b_g_r[color], 1)
        drawing = False
        region[color].append((x, y))
        color += 1


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)
# 上边就是框头尾的GUI了噢


# 执行了噢
print("依次框定头,尾,角点的颜色：(键入\'s\'以开始，\'e\'以结束)")
while True:
    _, img = CAP.read()
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('s'):
        print('s')
        break
img_copy = img.copy()
while True:
    cv2.imshow('image', img_copy)
    if cv2.waitKey(1) == ord('e') or color == 3:
        print('e')
        break
cv2.destroyAllWindows()
# 执行完了噢


# 知道框框位置了噢
blue, green, red = [img[
                    region[i][0][1] + 1:region[i][1][1] - 1,
                    region[i][0][0] + 1:region[i][1][0] - 1
                    ] for i in range(3)]

# while True:
#     cv2.imshow("b", blue)
#     cv2.imshow("g", green)
#     cv2.imshow("r", red)
#     if cv2.waitKey(1) == ord('q'):
#         break



# 计算当前情况下所需的bgr颜色在hsv色彩空间的取值范围
b_hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
g_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
r_hsv = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
b_mean_hsv, g_mean_hsv, r_mean_hsv = [clr.mean(axis=0).mean(axis=0) for clr in (b_hsv, g_hsv, r_hsv)]
print("头,尾,角点的平均hsv值：", '\n', b_mean_hsv, '\n', g_mean_hsv, '\n', r_mean_hsv)



offset_r = 12
offset = 12
lower_b, upper_b = b_mean_hsv - offset, b_mean_hsv + offset
lower_g, upper_g = g_mean_hsv - offset, g_mean_hsv + offset
lower_r, upper_r = r_mean_hsv - offset_r, r_mean_hsv + offset_r
lower_b[1] = lower_g[1] = lower_r[1] = 128
lower_b[2] = lower_g[2] = lower_r[2] = 46
upper_b[1] = upper_g[1] = upper_b[2] = upper_g[2] = upper_r[1] = upper_r[2] = 255



# 最终得到3个颜色识别函数了噢
kernel = np.ones((5, 5), np.uint8)


def Thresh_green(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_g, upper_g)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    return mask


def Thresh_blue(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_b, upper_b)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    return mask


def Thresh_red(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_r, upper_r)
    if lower_r[0] < 0:
        lower_r_2 = lower_r.copy()
        lower_r_2[0] += 180

        upper_r_2 = np.array([180, 255, 255], dtype=type(lower_r_2[0]))

        mask2 = cv2.inRange(hsv, lower_r_2, upper_r_2)
        mask = cv2.bitwise_or(mask, mask2)

    mask = cv2.erode(mask, kernel, iterations=3)
    mask = cv2.dilate(mask, kernel, iterations=4)
    return mask

#
# def Thresh_red(img):
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     mask = cv2.inRange(hsv, np.array([0,128,46]), np.array([15,255,255]))
#     mask2 = cv2.inRange(hsv,np.array([164,128,46]), np.array([180,255,255]))
#     mask = cv2.bitwise_or(mask, mask2)
#
#     mask = cv2.erode(mask, kernel, iterations=4)
#     mask = cv2.dilate(mask, kernel, iterations=4)
#     return mask

# while True:
#     _, img = CAP.read()
#     th_b = Thresh_blue(img)
#     th_g = Thresh_green(img)
#     th_r = Thresh_red(img)
#
#     cv2.imshow("img",img)
#
#     cv2.imshow("th_b",th_b)
#     cv2.imshow("th_g", th_g)
#     cv2.imshow("th_r", th_r)
#     if cv2.waitKey(1)==ord('q'):
#         break