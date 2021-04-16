from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import  numpy as np
#DOC HINH ANH
image=Image.open('anh.png')
plt.imshow(image)
"""
Hien thi kich thuoc:image.size
Hien thi dinh dang anh:image.format
Hien thi loai mau duoc su dung image.mode
"""
#Luu hinh anh
image.save("anhnew.jpg")
#Cat hinh anh
left=100
top=150
right=400
bottom=400
crop_image=image.crop((left,top,right,bottom))
crop_image.show()