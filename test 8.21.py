import numpy as np
import cv2 as cv

# 创建黑色的图像

img = np.zeros((512,512,3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img,(0,0),(511,511),(0,0,255),5)
cv.rectangle(img,(21,21),(255,255),(0,250,0),5)
cv.circle(img,(100,100),55,(250,0,0),-1)
cv.ellipse(img,(255,256),(100,50),0,0,360,(0,255,0),-1)

cv.namedWindow("111",cv.WINDOW_NORMAL)

cv.imshow("111",img)

cv.waitKey(0)

cv.destroyAllWindows()  #test 131