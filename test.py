import numpy as np
import cv2 as cv

img = cv.imread('sample.jpg', 1)  # 读取彩色图像
new_width = 800
new_height = 600
resized_image = cv.resize(img, (new_width, new_height))

cv.imshow("nihao2",resized_image)

imgray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY) # 转化为灰度图像

ret, thresh = cv.threshold(imgray, 180, 255, 0) #应用二值化阈值灰度图片

cv.imshow('Thresh', thresh) #画完轮廓后的图片

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #查找轮廓

area_threshold = 5000 # 设置阈值，用于排除小于该面积的轮廓

# 在检测到的图形周围绘制矩形轮廓，排除小于阈值的轮廓
for contour in contours:
    area = cv.contourArea(contour)
    if area > area_threshold:
        x, y, w, h = cv.boundingRect(contour)
        #cv.rectangle(resized_image, (x, y), (x + w, y + h), (0, 255, 0), 2) #直接绘制矩形
        rect = cv.minAreaRect(contour)
        box = cv.boxPoints(rect) #矩形的四个角
        box = np.int0(box)
        cv.drawContours(resized_image, [box], 0, (0, 255, 0), 3) # -(中心(x,y)，(宽度，高度)，旋转角度)

cv.imshow('Contours', resized_image) #画完轮廓后的图片

k = cv.waitKey(0)
if k == 27:         # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
    cv.imwrite('sample.png', resized_image)
    cv.destroyAllWindows()