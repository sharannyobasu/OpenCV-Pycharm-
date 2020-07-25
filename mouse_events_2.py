#HOW TO DRAW CIRCLES IN OPENCV AND DRAW LINES BETWEEN EVERY CLICKED POINT
'''import numpy as np
import cv2
def click_event(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3
                   , (0,0,255), -1) #-1 thickness just fills the shape
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        #font=cv2.FONT_HERSHEY_COMPLEX
        cv2.imshow("image", img)
#img=cv2.imread("lena.jpg")
img=np.zeros((512,512,3), np.uint8)
cv2.imshow("image", img)
points=[]
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#HOW TO PICK THE COLOUR IN THE CLICKED COORDINATE AND DISPLAY IT
import numpy as np
import cv2
def click_event(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        #cv2.circle(img, (x,y),3, (0,0,255), -1)
        mycolorImage=np.zeros((512,512,3), np.uint8)
        mycolorImage[:]=[blue,green,red]
        cv2.imshow("color", mycolorImage)
        #cv2.imshow("lena", img)
img=cv2.imread("lena.jpg")
#img=np.zeros((512,512,3), np.uint8)
cv2.imshow("image", img)
points=[]
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
