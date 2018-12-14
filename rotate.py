# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
from imutils import resize
import matplotlib.pyplot as plt

def rotate(img,radius,head_location,tail_location):
    head_position_x=head_location[0]
    head_position_y=head_location[1]
    tail_position_x=tail_location[0]
    tail_position_y=tail_location[1]
    if(head_position_x==tail_position_x)delta=1.57
    else delta=math.atan((head_position_y-tail_position_y)*1.0/(head_position_x-tail_position_x))
    tmp=[head_position_x+radius*math.cos(delta),head_position_y+radius*math.sin(delta)]
    if(edge_test(img,tmp))return 0;                                      #go ahead
    for i in range (1,90,1):
        tmp=[head_position_x+radius*math.cos(delta+1),head_position_y+radius*math.sin(delta+1)]            #left
        if(edge_test(img,tmp))return 1;
    for i in range (1,90,1):
        tmp=[head_position_x+radius*math.cos(delta-1),head_position_y+radius*math.sin(delta-1)]            #right
        if(edge_test(img,tmp))return 2;




def edge_test(img,location):
    x=location[0]
    y=location[1]
    C_A = img[[y-1,y,y+1]]
    C_A = C_A[:,[x-1,x,x+1]]
    if(sum(sum(C_A))==2295)return true;
    else return false;
