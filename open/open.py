import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pathlib
import os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))

data_dir = pathlib.Path(cwd + "/img")

all_img = (list(data_dir.glob('*/*.jpg')))


img = mpimg.imread(str(all_img[0]))

print(all_img[0])

imgplot = plt.imshow(img)
plt.show()