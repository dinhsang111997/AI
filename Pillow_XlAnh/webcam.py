import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640) #set kich thuoc theo chieu rong
cap.set(4,720)
cap.set(10,200)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break