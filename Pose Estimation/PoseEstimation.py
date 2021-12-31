import cv2
import mediapipe as mp
import time
mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()

cap=cv2.VideoCapture('dancing1 video.mp4')

frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
frame_size=(frame_width,frame_height)
fps=20
output=cv2.VideoWriter('output_poseEstimation.avi',cv2.VideoWriter_fourcc('M','J','P','G'),20,frame_size)

pTime=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c=img.shape
            print(id, lm)
            if id==12:
                cx,cy=int(lm.x*w),int(lm.y*h)
                cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    output.write(img)
    cv2.imshow('image', img)
    cv2.waitKey(1)
output.release()
