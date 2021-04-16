from PIL import Image
import os

size=(300,300)
for f in os.listdir('.'):#'.'thu muc hien tai
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)

        i.thumbnail(size)
        i.save('Size/{}_300{}'.format(fn,fext))