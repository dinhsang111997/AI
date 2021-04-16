from PIL import Image
import numpy as np
from pylab import *
im=np.asarray(Image.open('anh.jpg'))
x=[100,100,400,400]
y=[200,500,200,500]
plot(x,y,"r*")
plot(x[:2],y[:2])
title('Plotting:"empire.jpg"')
show()