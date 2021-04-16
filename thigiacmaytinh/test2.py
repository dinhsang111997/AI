import cv2

def get_value(pos):
    get_value.value=pos
get_value.value=0

cv2.namedWindow("Control")
cv2.createTrackbar("Value","Control",128,255,get_value)
while True:
    img = cv2.imread("anh.png",0)
    cv2.imshow("Control",img)

    img=cv2.threshold(img,get_value.value,255,cv2.THRESH_BINARY)[1]
    cv2.imshow("Image",img)
    if cv2.waitKey(10)==ord('q'):
        break
cv2.destroyAllWindows()