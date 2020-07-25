import cv2
img = cv2.imread("lena.jpg", 1)
print(img)
cv2.imshow("image", img)
k=cv2.waitKey(0)
if k==ord("s"):
    cv2.destroyAllWindows()
cv2.imwrite("lena_copy.jpg", img)