import cv2
import datetime
cap=cv2.VideoCapture(0) #0 means your default camera(webcam)

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        datetime1=str(datetime.datetime.now())
        frame=cv2.putText(frame,datetime1,(10,50), font, 1,(0,255,255),2,cv2.LINE_AA)
        #print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        if(cv2.waitKey(1)) & 0xFF ==ord("q"): #here q is case sensitive
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()