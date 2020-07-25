import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask= cv2.threshold(img, 220,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((5,5), np.uint8)

dilation=cv2.dilate(mask,kernel, iterations=2)
erosion=cv2.erode(mask, kernel, iterations=2)
titles=["image", "mask", "dilation", "erosion"]
images=[img,mask,dilation,erosion]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


