from PIL import  Image
import os
pil_im=Image.open('anh.jpg').convert('L')
#pil_im.thumbnail((128,128))
#giam kich thuoc hinh anh
box=(100,100,400,400)
region=pil_im.crop(box)
#Cắt một vùng của hình anh sử dụng hàm crop

#region=region.transpose(Image.ROTATE_180)
#Xoay hinh anh mot goc 180 do va gan vao hinh anh cu
#pil_im.paste(region,box)


#Thay doi kich thuoc va xoay
out = pil_im.resize((128,128)).rotate(45)
#out = pil_im.rotate(45)


#pil_im.show()
out.show()
#region.show()