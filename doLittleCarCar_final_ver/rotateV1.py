# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
from imutils import resize
import matplotlib.pyplot as plt

def rotate(img,radius1,init_radius2,end_radius2,step,head_location,tail_location):
    ret = 'A'
    for i in range(init_radius2,end_radius2,step):
        
        left,mid,right=get_sensor(radius1, i, head_location, tail_location)
        if(edge_test(img, left)):
            ret = 'L'
        elif (edge_test(img, right)):
            ret = 'R'
        else:
            ret = 'A'
    return ret, left, mid, right

# def rotate(img,radius1,radius2,head_location,tail_location):
def get_sensor(radius1, radius2, head_location, tail_location):
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

    l = [int(left_x), int(left_y)]
    m = [int(mid_x), int(mid_y)]
    r = [int(right_x), int(right_y)]
    # print(2)
    return l,m,r

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
