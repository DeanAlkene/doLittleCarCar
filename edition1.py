# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
from imutils import resize
import matplotlib.pyplot as plt
#def rotate(img,radius1,radius2,head_location,tail_location):
def rotate(img,radius1,radius2,head_location,tail_location):
    head_position_x=head_location[0]
    head_position_y=head_location[1]
    tail_position_x=tail_location[0]
    tail_position_y=tail_location[1]
    dx=head_position_x-tail_position_x
    dy=head_position_y-tail_position_y
    dr=math.sqrt(dx**2+dy**2)
    if(head_position_x==tail_position_x):
        conste=(head_position_y-tail_position_y)/abs(head_position_y-tail_position_y)
        mid_y=head_position_y+radius1*conste
        mid_x=head_position_x
        right_x=mid_x-radius2*conste
        right_y=left_y=mid_y
        left_x=mid_x+radius2*conste
    else:
        mid_x=head_position_x+radius1*dx/dr
        mid_y=head_position_y+radius1*dy/dr
        right_x=mid_x-radius2*dy/dr
        right_y=mid_y+radius2*dx/dr
        left_x=mid_x+radius2*dy/dr
        left_y=mid_y-radius2*dx/dr
    boolmid=edge_test(img,[mid_x,mid_y])
    boolleft=edge_test(img,[left_x,left_y])
    boolright=edge_test(img,[right_x,right_y])
    if((not boolright) and (not boolleft)):
        return 'A'
    if(boolleft):
        return 'R'     #N
    if(boolright):
        return 'L'     #M


def edge_test(img,location):
    x=location[0]
    y=location[1]
    C_A = img[[y-1,y,y+1]]
    C_A = C_A[:,[x-1,x,x+1]]
    if(np.sum(C_A)==2295):
        return true
    else:
        return false
