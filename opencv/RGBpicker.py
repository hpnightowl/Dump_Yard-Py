import cv2 as cv
import numpy as np

def just(x):
    pass
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('img')
cv.createTrackbar('B','img',0,255, just )
cv.createTrackbar('G','img',0,255, just )
cv.createTrackbar('R','img',0,255, just )

while True:
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF 
    if k ==27:  #27 for pressing escape key
        break
    b= cv.getTrackbarPos('B','img')
    g= cv.getTrackbarPos('G','img')
    r= cv.getTrackbarPos('R','img')

    img[:] = [b,g,r]
cv2.destroyAllWindows()
