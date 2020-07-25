import cv2
import numpy as np
def nothing(x):
    print(x)

#img=np.zeros((300,512,3), np.uint8)
cv2.namedWindow("image")  #use to create a window with a name
cv2.createTrackbar("cp", "image", 10,400, nothing)

switch="color/gray"
cv2.createTrackbar(switch, "image", 0,1,nothing)
while(1):
    img = cv2.imread("lena.jpg")

    pos=cv2.getTrackbarPos("cp", "image")
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50,150), font, 4, (0,0,255), 10)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    #b=cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    #r = cv2.getTrackbarPos("R", "image")
    #s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        pass
    else:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow("image", img)
    #img[:]=[b,g,r]
cv2.destroyAllWindows()