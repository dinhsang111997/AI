from PIL import Image
import os
img1=Image.open('anh.jpg')
img1.rotate(60).show()