from PIL import Image
import os
img1=Image.open('anh.jpg')
#Chuyen doi cac thang mau cua anh
img1.convert(mode='L').show()
#https://pillow.readthedocs.io/en/stable/handbook/concepts.html