import numpy as np
import cv2

img=cv2.imread("shapes.jpg")
imGrey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh=cv2.threshold(imGrey, 240, 255, cv2.THRESH_BINARY)
contours, _=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    if len(approx)==3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==4:
        (x1,y1,w,h)=cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio >=0.85 and aspectratio<=1.15:
            cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
    elif len(approx)==5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==6:
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==7:
        cv2.putText(img, "Heptagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==8:
        cv2.putText(img, "Octagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==9:
        cv2.putText(img, "Nonagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    elif len(approx)==10:
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()