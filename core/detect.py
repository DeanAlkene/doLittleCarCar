import cv2
import color
import numpy as np

# 找到轮廓点集
def find_cnts(closed):
    (_, cnts, _) = cv2.findContours(closed.copy(),
                                    # 参数二：轮廓类型
                                    cv2.RETR_EXTERNAL,             #表示只检测外轮廓
                                    # cv2.RETR_CCOMP,                #建立两个等级的轮廓,上一层是边界
                                    # cv2.RETR_LIST,                 #检测的轮廓不建立等级关系
                                    # cv2.RETR_TREE,                 #建立一个等级树结构的轮廓
                                    # 参数三：处理近似方法
                                    # cv2.CHAIN_APPROX_NONE,         #存储所有的轮廓点，相邻的两个点的像素位置差不超过1
                                    cv2.CHAIN_APPROX_SIMPLE,         #例如一个矩形轮廓只需4个点来保存轮廓信息
                                    # cv2.CHAIN_APPROX_TC89_L1,
                                    # cv2.CHAIN_APPROX_TC89_KCOS
                                    )
    return cnts

# 从轮廓点集得到bounding box
def get_box(c):
    rect = cv2.minAreaRect(c)
    return np.int0(cv2.boxPoints(rect))


# 找小车车
def detect_car(img):
    cnts_green = find_cnts(color.Thresh_green(img))
    cnts_blue = find_cnts(color.Thresh_blue(img))

    try:#如果没有找到小车车的话就retrun None, 在main里处理
        c_green = sorted(cnts_green, key=cv2.contourArea, reverse=True)[0]
        c_blue = sorted(cnts_blue, key=cv2.contourArea, reverse=True)[0]
    except:
        return None

    box_green = get_box(c_green)
    box_blue = get_box(c_blue)

    head = sum(box_green) // 4
    tail = sum(box_blue) // 4

    return box_green, head, box_blue, tail


# 检测角点
def detect_corners(img):
    RED = color.Thresh_red(img)
    cnts_red = find_cnts(RED)
    try:
        sorted_cnts = sorted(cnts_red, key=cv2.contourArea, reverse=True)
        c_red = [sorted_cnts[i] for i in range(4)] # bug: sort_cnts[0:4]
    except:
        return None
    red_box = [get_box(c) for c in c_red]
    return [sum(r_b) // 4 for r_b in red_box]


# sort corners as (1, 2)
#                 (3, 4)
def sorted_corners(corners):
    corners = sorted(corners, key=lambda c: sum(c))
    if corners[1][0] < corners[2][0]:
        corners[1], corners[2] = corners[2], corners[1]
    return corners