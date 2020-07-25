import cv2
import numpy as np
img1=np.zeros((350,350,3), np.uint8)
img11=cv2.rectangle(img1, (170,0), (300,100),(255,255,255), -1)
img2=cv2.rectangle(img1, (200,0), (300,300),(255,255,255), -1)
#img2=cv2.imread("imread", img1)
cv2.imshow("img1", img1)
bitand=cv2.bitwise_and(img11,img2)
cv2.imshow("bitand", bitand)
cv2.waitKey(0)
cv2.destroyAllWindows()