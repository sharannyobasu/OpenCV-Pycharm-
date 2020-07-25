import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img, cv2.CV_64F, ksize=1)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img, cv2.CV_64F, 1,0)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=cv2.Sobel(img, cv2.CV_64F, 0,1)
sobelY=np.uint8(np.absolute(sobelY))
canny=cv2.Canny(img, 100, 200)

sobelCombined=cv2.bitwise_or(sobelY, sobelX)

titles=["image", "laplacian", "SobelX", "SobelY", "Combined", "canny"]
images=[img, lap, sobelX, sobelY, sobelCombined, canny]
for i in range(6):
    plt.subplot(3,2,i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()