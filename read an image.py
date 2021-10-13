import numpy as np
import matplotlib.pyplot as plt
from numpy import binary_repr as binr
# from matplotlib import imread


image = plt.imread('sdpj.tiff')[:,:,:3]
plt.imshow(image)
