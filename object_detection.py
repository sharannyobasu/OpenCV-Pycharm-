import numpy as np
import cv2
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0,255,nothing)
cv2.createTrackbar("LS", "Tracking", 0,255,nothing)
cv2.createTrackbar("LV", "Tracking", 0,255,nothing)
cv2.createTrackbar("UH", "Tracking", 255,255,nothing)
cv2.createTrackbar("US", "Tracking", 255,255,nothing)
cv2.createTrackbar("UV", "Tracking", 255,255,nothing)
while True:
    #frame=cv2.imread("smarties.png")
    _, frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")
    hh = cv2.getTrackbarPos("UH", "Tracking")
    hs = cv2.getTrackbarPos("US", "Tracking")
    hv = cv2.getTrackbarPos("UV", "Tracking")
    lb=np.array([lh,ls,lv])
    ub=np.array([hh,hs,hv])
    #threshold to get the blue color
    mask=cv2.inRange(hsv, lb,ub)  #only detects the postion which contains the color in range lb and ub and displays in b/w
    res=cv2.bitwise_and(frame, frame,mask=mask) #source1, source2, mask variable (mask in this case)
    cv2.imshow("image", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res) #shows the union of the b/w mask detected and the entire original image

    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()