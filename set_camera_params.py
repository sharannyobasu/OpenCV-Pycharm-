import cv2
cap=cv2.VideoCapture(0) #0 means your default camera(webcam)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #default height is 480
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #default width is 640

cap.set(3,1208) #3 is the propId for camera width 1208 is the pixels
cap.set(4,720) #4 is the propId for camera height. 720 is the pixels
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text="Width: "+str(cap.get(3)) + " Height :"+str(cap.get(4))
        frame=cv2.putText(frame, text,(10,50), font, 1,(0,255,255),2,cv2.LINE_AA)
        #print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        if(cv2.waitKey(1)) & 0xFF ==ord("q"): #here q is case sensitive
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()