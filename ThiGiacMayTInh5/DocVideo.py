import cv2
import time
cap=cv2.VideoCapture('Video.mp4')
fps=cap.get(cv2.CAP_PROP_FPS)
wait_time=1000/fps
while True:
    pre_time=time.time()
    ret,img=cap.read()
    cv2.imshow("Video",img)
    delta_time=(time.time()-pre_time)*1000
    if delta_time>wait_time:
        delay_time=1
    else:
        delay_time=wait_time-delta_time
    if cv2.waitKey(int(delay_time))==ord('q'):
        break
cv2.destroyAllWindows()