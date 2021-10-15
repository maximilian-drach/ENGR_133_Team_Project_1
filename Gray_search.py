import numpy as np
import matplotlib.pyplot as plt

def grey(image):

    grey_values = (image[:,:,0]*.299 + image[:,:,1]*.587 + image[:,:,2]*.114)
    grey = image.copy()
    for i in range(3):
        grey[:,:,i] = grey_values

    return grey


def earth_finder(grey_image):
    grey



def float64_uint8(img):
    #gets the max number the data could be
    img_data_max = np.iinfo(img.dtype).max
    img = img.astype(np.float64)/img_data_max
    img = 255*img
    img = img.astype(np.uint8)

    return img


def uint8_float64(img):
    img_data_max = np.iinfo(img.dtype).max
    img = img.astype(np.unit8)/img_data_max
    img = img.astype(np.float64)

    return img



image = plt.imread('image.tiff')[:,:,:3]
image = grey(image)
plt.imsave('gray.tiff', image)
