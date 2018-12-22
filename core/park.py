# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math

def park(head_point,destination_point,trigger_radius):
    if((head_point[0]-destination_point[0])**2+(head_point[1]-destination_point[1])**2<trigger_radius**2):
        return 'P'
    else:
        return ''