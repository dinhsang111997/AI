import cv2
import time

cap = cv2.VideoCapture('VIDEO2.mp4')
fps=cap.get(cv2.CAP_PROP_FPS)
wait_time=1000/fps
while(cap.isOpened()):
    #Đọc video
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(int(wait_time)) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()