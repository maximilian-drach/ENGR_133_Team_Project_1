import numpy as np
import matplotlib.pyplot as plt

def grey(image):

    grey_values = (image[:,:,0]*.299 + image[:,:,1]*.587 + image[:,:,2]*.114)
    grey = image.copy()
    for i in range(3):
        grey[:,:,i] = grey_values

    return grey


def earth_finder(grey_image):
    #gets the brighest spot on the image
    brightest_spot = np.amax(grey_image)
    #finds the index whete the maximum value is
    index_max = np.where(grey_image == brightest_spot)
    #takes where first items of each list return, the turns the tupple to a list
    cordinates = list(zip(index_max[0], index_max[1]))
    #since all rgb values are the same, we only need the first item of the list
    return cordinates[0]
    

def earth_image(grey_image, location):
    earth = np.

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
earth_location = earth_finder(image)

#plt.imsave('gray.tiff', image)
