# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:41:56 2021

@author: ashli
"""

import numpy as np
import matplotlib.pyplot as plt

image=plt.imread('Pale_Blue_Dot_Encrypted.tiff')
image=(image*255).astype(np.uint8)

plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1))
plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1))
plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1))
