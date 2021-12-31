import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture("D:\CVAIproject\kidsplaying.webm")
pTime=0

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
frame_size=(frame_width,frame_height)
fps=20
output=cv2.VideoWriter('outputx.avi',cv2.VideoWriter_fourcc('M','J','P','G'),20,frame_size)

mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection()

while True:
    success,img=cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=faceDetection.process(imgRGB)
    #print(results)


    if results.detections:
        for id,detection in enumerate(results.detections):
            #mpDraw.draw_detection(img,detection)
            #print(id,detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            bboxC=detection.location_data.relative_bounding_box
            ih,iw,ic=img.shape
            bbox=int(bboxC.xmin*iw),int(bboxC.ymin*ih), \
                 int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(img,bbox,(255,0,255),2)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,
                        3, (0,0, 255), 2)



    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS: {int(fps)}', (20,70),cv2.FONT_HERSHEY_PLAIN,
                3,(0,255,0),2)
    output.write(img)
    cv2.imshow('Image', img)
    cv2.waitKey(10)
 output.release()
