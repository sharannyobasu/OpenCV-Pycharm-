import cv2
import numpy as np

img=cv2.imread("sudoku.png",0)
th1=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2);
th2=cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2);

cv2.imshow("original", img)
cv2.imshow("updated", th1)
cv2.imshow("updated_gaussian", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()