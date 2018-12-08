import cv2
import color
import numpy as np

# 找到轮廓点集
def find_cnts(closed):
    (_, cnts, _) = cv2.findContours(closed.copy(),
                                    cv2.RETR_LIST,
                                    cv2.CHAIN_APPROX_SIMPLE)
    return cnts

# 从轮廓点集得到bounding box
def get_box(c):
    rect = cv2.minAreaRect(c)
    return np.int0(cv2.boxPoints(rect))


# 找小车车
def detect_car(img):
    cnts_green = find_cnts(color.Thresh_green(img))
    cnts_blue = find_cnts(color.Thresh_blue(img))

    try:#如果没有找到小车车的话就抛出异常，然后重来
        c_green = sorted(cnts_green, key=cv2.contourArea, reverse=True)[0]
        c_blue = sorted(cnts_blue, key=cv2.contourArea, reverse=True)[0]
    except:
        return None

    box_green = get_box(c_green)
    box_blue = get_box(c_blue)

    head = sum(box_green) // 4
    tail = sum(box_blue) // 4

    return box_green, head, box_blue, tail


# 找透视变换的4个点
def detect_corners(img):
    cnts_red = find_cnts(color.Thresh_red(img))
    try:
        sorted_cnts = sorted(cnts_red, key=cv2.contourArea, reverse=True)
        c_red = [sorted_cnts[i] for i in range(4)] # bug: sort_cnts[0:4]
    except:
        return None
    red_box = [get_box(c) for c in c_red]
    return [sum(r_b) // 4 for r_b in red_box]


def sorted_corners(corners):
    corners = sorted(corners, key=lambda c: sum(c))
    if corners[1][0] < corners[2][0]:
        corners[1], corners[2] = corners[2], corners[1]
    return corners