# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
from imutils import resize
import matplotlib.pyplot as plt


# def rotate(img,radius1,radius2,head_location,tail_location):
def rotate(img, radius1, radius2, head_location, tail_location, oldOp):
    head_position_x = head_location[0]
    head_position_y = head_location[1]
    tail_position_x = tail_location[0]
    tail_position_y = tail_location[1]
    dx = head_position_x - tail_position_x
    dy = head_position_y - tail_position_y
    dr = math.sqrt(dx ** 2 + dy ** 2)
    if (head_position_x == tail_position_x):
        conste = (head_position_y - tail_position_y) / abs(head_position_y - tail_position_y)
        mid_y = head_position_y + radius1 * conste
        mid_x = head_position_x
        right_x = mid_x - radius2 * conste
        right_y = left_y = mid_y
        left_x = mid_x + radius2 * conste
    else:
        mid_x = head_position_x + radius1 * dx / dr
        mid_y = head_position_y + radius1 * dy / dr
        right_x = mid_x - radius2 * dy / dr
        right_y = mid_y + radius2 * dx / dr
        left_x = mid_x + radius2 * dy / dr
        left_y = mid_y - radius2 * dx / dr
    # print([left_x,left_y],[right_x,right_y])
    try:
        boolmid = edge_test(img, [mid_x, mid_y])
    except:
        boolmid = False
    try:
        boolleft = edge_test(img, [left_x, left_y])
    except:
        boolleft = False
    try:
        boolright = edge_test(img, [right_x, right_y])
    except:
        boolright = False
    # print([boolleft, boolmid, boolright])
    l = [int(left_x), int(left_y)]
    m = [int(mid_x), int(mid_y)]
    r = [int(right_x), int(right_y)]
    # print(2)
    ret = 'A'
    
    if oldOp == 'R':
        if boolmid:
            ret = 'A'
        elif boolright:
            ret = 'R'
        elif boolleft:
            ret = 'L'
        else:
            ret = 'R'
    elif oldOp == 'L':
        if boolmid:
            ret = 'A'
        elif boolright:
            ret = 'R'
        elif boolleft:
            ret = 'L'
        else:
            ret = 'L'
    else:
        if boolright:
            ret = 'R'
        elif boolleft:
            ret = 'L'
        else:
            ret = 'A'

    return ret,l,m,r

def edge_test(img, location):
    x = int(location[0])
    y = int(location[1])
    sum_t = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            sum_t += img[y + i][x + j]
    if (sum_t > 1500):
        return True
    else:
        return False
