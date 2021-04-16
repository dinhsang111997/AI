import  cv2
import numpy as np
img=np.zeros((600,600,3))
img[:,:,2]=255
img[250:350,100:500,:]=255
img[100:500,250:350,:]=255
cv2.imshow("Image",img)
cv2.waitKey()