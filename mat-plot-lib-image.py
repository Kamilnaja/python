import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
img = np.asarray(Image.open('./img-classification/pictures/analog/-original-imagcvgadpwxzhc3.jpeg'))

imgplot = plt.imshow(img)
lum_img = img[:, :, 0]
plt.imshow(lum_img)
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.colorbar()
plt.show()