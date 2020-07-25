import cv2
import numpy as np

img=cv2.imread("gradient.png",0)
_, th1=cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
_, th2=cv2.threshold(img, 127,255, cv2.THRESH_TRUNC)


cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()