import numpy as np
print('I an SB')
print('yes')
import cv2 as cv
# import cv2 as cv
img=cv.imread('sample.jpg',1)
cv.namedWindow('111',cv.WINDOW_NORMAL)
cv.imshow('111',img)
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.waitKey(0)
cv.destroyAllWindows()
