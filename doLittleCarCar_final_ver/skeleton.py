import cv2
from imutils import resize
from imutils.contours import sort_contours
from skimage.morphology import skeletonize as skl
import numpy as np

def skeleton_endpoints(skel):
    skel = skel.copy()
    skel[skel != 0] = 1
    skel = np.uint8(skel)

    kernel = np.uint8([[1,  1, 1],
                       [1, 10, 1],
                       [1,  1, 1]])
    src_depth = -1
    filtered = cv2.filter2D(skel, src_depth,kernel)

    out = np.zeros_like(skel)
    out[np.where(filtered == 11)] = 1
    rows, cols = np.where(filtered == 11)
    coords = list(zip(cols, rows))
    return coords

def Skeleton(img):
    img = cv2.GaussianBlur(img, (3, 3), 10)
    img = resize(img, width=700)

    img = cv2.GaussianBlur(img, (3, 3), 3)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret,th = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
    th = cv2.bitwise_not(th)

    kernel = np.array([[0, 1, 1],
                      [0, 1, 0],
                      [1, 1, 0]], dtype='uint8')

    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)


    th = th == 255
    th = skl(th)
    th = th.astype(np.uint8)*255

    _, contours, _ = cv2.findContours(th.copy(), cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_NONE)
    contours, _ = sort_contours(contours, )

    endpoints = []
    skeletons = []

    for contour in contours:
        if cv2.arcLength(contour, True) > 100:
            mask = np.zeros(img.shape, np.uint8)
            x, y, w, h = cv2.boundingRect(contour)
            mask[y:y+h, x:x+w] = 255
            mask = cv2.bitwise_and(mask, th)
            rows, cols = np.where(mask == 255)
            skeletons.append(list(zip(cols, rows)))

            eps = skeleton_endpoints(mask)
            endpoints.append(eps)

    return th

def get_origin(address):
    img=cv2.imread(address,0)
    img = cv2.GaussianBlur(img, (3, 3), 10)
    img = resize(img, width=700)

    img = cv2.GaussianBlur(img, (3, 3), 3)
    return img
