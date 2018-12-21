# import detect
import cv2
import numpy as np

l = [1,2,3]
print(sorted(l, key=lambda x: x))
exit(0)

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


kernel = np.ones((5,5),np.uint8)
lower_r = np.array([0,128,46])
upper_r = np.array([10,255,255])
def Thresh_red(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_r, upper_r)
    mask = cv2.erode(mask, kernel, iterations=4)
    mask = cv2.dilate(mask, kernel, iterations=4)
    return mask

# 检测角点
def detect_corners(img):
    cnts_red = find_cnts(Thresh_red(img))
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

cap = cv2.VideoCapture(1)

while cap.isOpened():
    _,img=cap.read()
    corners = detect_corners(img)
    if corners is None:
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            break
        continue


    corners = sorted_corners(corners)
    print(corners)

    if corners is None:
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait(1) 以实现在查找失败时，瞬间进入下一循环继续查找
            break