import cv2
import time

cv2.namedWindow("Control")


cap=cv2.VideoCapture('Video.mp4')
fps=cap.get(cv2.CAP_PROP_FPS)
wait_time=1000/fps

play=True
while True:
    pre_time=time.time()
    if play:
        ret,img=cap.read()
    if ret==False:
        break
    cv2.imshow("Video",img)
    delta_time=(time.time()-pre_time)*1000
    if delta_time>wait_time:
        delay_time=1
    else:
        delay_time=wait_time-delta_time
    key=cv2.waitKey(int(delay_time))
    if key==ord('q'):
        break
    if key==ord(' '):
        play=not play
cv2.destroyAllWindows()