# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
from imutils import resize
import matplotlib.pyplot as plt

def park(head_point,destination_point,trigger_radius):
    print(head_point,destination_point,trigger_radius)
    if((head_point[0]-destination_point[0])**2+(head_point[1]-destination_point[1])**2<trigger_radius**2):
        return 'P'
    else:
        return 'W'

# head=[1,2]
# tail=[2,4]
# print(park(head,tail,1))
