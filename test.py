# import cv2
# import numpy as np
# from image_processing import *
#
#
# # 根据线段端点计算对应直线交点，原理参考直线点斜式方程联立所解
# def CrossPoint(line1, line2):
#     x0, y0, x1, y1 = line1[0]
#     x2, y2, x3, y3 = line2[0]
#
#     dx1 = x1 - x0
#     dy1 = y1 - y0
#
#     dx2 = x3 - x2
#     dy2 = y3 - y2
#
#     D1 = x1 * y0 - x0 * y1
#     D2 = x3 * y2 - x2 * y3
#
#     y = float(dy1 * D2 - D1 * dy2) / (dy1 * dx2 - dx1 * dy2)
#     x = float(y * dx1 - D1) / dy1
#
#     return (int(x), int(y))
#
#
# def SortPoint(points):
#     sp = sorted(points, key=lambda x: (int(x[1]), int(x[0])))
#     if sp[0][0] > sp[1][0]:
#         sp[0], sp[1] = sp[1], sp[0]
#
#     if sp[2][0] > sp[3][0]:
#         sp[2], sp[3] = sp[3], sp[2]
#
#     return sp
#
#
# def perspective_transformation(img):
#     width, height = img.shape[0:2]
#
#     gray = Gray(img)
#     blurred = GaussianBlur(gray)
#     Cannying = cv2.Canny(blurred,35,189)
#
#     lines = cv2.HoughLinesP(Cannying, 1, np.pi / 180, threshold=30, minLineLength=320, maxLineGap=40)
#
#     for i in range(int(np.size(lines) / 4)):
#         for x1, y1, x2, y2 in lines[i]:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
#
#     # 根据上述霍夫变换获得的线段求直线交点，实验证明，霍夫变换获取并存储直线时是横纵方向依次完成的，即只需如下形式计算
#     points = np.zeros((4, 2), dtype="float32")
#     points[0] = CrossPoint(lines[0], lines[2])
#     points[1] = CrossPoint(lines[0], lines[3])
#     points[2] = CrossPoint(lines[1], lines[2])
#     points[3] = CrossPoint(lines[1], lines[3])
#
#
#     sp = SortPoint(points)
#
#     dstrect = np.array([
#         [0, 0],
#         [width - 1, 0],
#         [0, height - 1],
#         [width - 1, height - 1]], dtype="float32")
#
#     transform = cv2.getPerspectiveTransform(np.array(sp), dstrect)  # 利用原图角点和目标角点计算透视变换矩阵
#
#     warpedimg = cv2.warpPerspective(img, transform, (width, height))
#
#     return warpedimg
#
#
# # cap = cv2.VideoCapture(0)
# #
# # while cap.isOpened():
# #     _, frame = cap.read()
#
# frame = cv2.imread("666.png")
#
# width, height = frame.shape[0:2]
#
# gray = Gray(frame)
# blurred = GaussianBlur(gray)
# Cannying = cv2.Canny(blurred, 35, 189)
#
# lines = cv2.HoughLinesP(Cannying, 1, np.pi / 180, threshold=30, minLineLength=320, maxLineGap=40)
#
# for i in range(int(np.size(lines) / 4)):
#     for x1, y1, x2, y2 in lines[i]:
#         cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)
#
# # 根据上述霍夫变换获得的线段求直线交点，实验证明，霍夫变换获取并存储直线时是横纵方向依次完成的，即只需如下形式计算
# points = np.zeros((4, 2), dtype="float32")
# points[0] = CrossPoint(lines[0], lines[2])
# points[1] = CrossPoint(lines[0], lines[3])
# points[2] = CrossPoint(lines[1], lines[2])
# points[3] = CrossPoint(lines[1], lines[3])
#
# sp = SortPoint(points)
#
# dstrect = np.array([
#     [0, 0],
#     [width - 1, 0],
#     [0, height - 1],
#     [width - 1, height - 1]], dtype="float32")
#
# transform = cv2.getPerspectiveTransform(np.array(sp), dstrect)  # 利用原图角点和目标角点计算透视变换矩阵
#
# warpedimg = cv2.warpPerspective(frame, transform, (width, height))
#
# cv2.imshow("pers",warpedimg)
#
# # if cv2.waitKey(1)&0xff == ord('q'):
# #     break
# #
# # cap.release()
# # cv2.destroyAllWindows()