import faces
import numpy as np 
#import imghdr
#import matplotlib.pyplot as plt
glass = open('/home/zhou/man.jpg','rb')
image = faces.FaceAppImage(file=glass)
glass = image.apply_filter('makeup',cropped = True)
with open('save.jpg','w') as f:
	f.writelines(glass)
#imghdr.what(glass)
#x = np.fromfile(str(glass),dtype=np.ubyte)

