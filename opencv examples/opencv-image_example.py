import cv2

image=cv2.imread('D:\TT.jpg')
while True:
    cv2.imshow('python marks',image)

    text="This is my college"
    cv2.putText(image,text,(5,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,255),2)
    cv2.rectangle(image,(30,60),(1325,600),(0,0,255),2)
    cv2.imwrite('tt_output_image.jpg',image)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows()

