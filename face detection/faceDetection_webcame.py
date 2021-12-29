import cv2
#face_cascade=cv2.CascadeClassifier('"D:\CVAIproject\haarcascade_frontalface_default.xml"')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)#web camera
#cap=cv2.VideoCapture('vidoefilename.mp4')

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,1)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        k=cv2.waitKey(1)
cap.release()
