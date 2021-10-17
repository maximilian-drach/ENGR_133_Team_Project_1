# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:41:56 2021

@author: ashli
"""

import numpy as np
import matplotlib.pyplot as plt

image=plt.imread('Pale_Blue_Dot_Encrypted.tiff')[:,:,:3]
def histogram(image):
    image=(image*255).astype(np.uint8)
    
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='red', alpha=.5, label='Red Pixels')
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='green', alpha=.5, label='Green Pixels')
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='blue', alpha=.5, label='Blue Pixels')
    plt.legend()
    
    return plt.legend
 
histogram(image)   

def new_key(phrase):
    