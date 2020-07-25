import cv2
import numpy as np

img=cv2.imread("lena.jpg")

'''lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr1=cv2.pyrUp(lr2)

cv2.imshow("Original", img)
cv2.imshow("Pyr Down 1", lr1)
cv2.imshow("Pyr Down 2", lr2)
cv2.imshow("Pyr Up 1", hr1)'''

#Making Pyramids using for loop

layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()