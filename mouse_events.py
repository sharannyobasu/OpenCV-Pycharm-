import numpy as np
import cv2
def click_event(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:

        font=cv2.FONT_HERSHEY_COMPLEX
        strxy="Left button"
        cv2.putText(img, strxy,(x,y), font, 1, (0,0,255), 1,cv2.LINE_AA)
        cv2.imshow("image", img)
    if event==cv2.EVENT_RBUTTONDOWN:
        font = cv2.FONT_HERSHEY_COMPLEX
        strxy = "Right button"
        cv2.putText(img, strxy, (x, y), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow("image", img)
img=cv2.imread("lena.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()