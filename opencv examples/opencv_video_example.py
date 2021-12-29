import cv2
import imutils

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame=cap.read()
    frame=imutils.resize(frame,width=1200)

    text="It's me bro"
    cv2.putText(frame,text,(5,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,255,255),2)
    cv2.rectangle(frame,(500,40),(1000,700),(0,0,255),2)
    if ret==True:
        cv2.imshow('application', frame)

        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()