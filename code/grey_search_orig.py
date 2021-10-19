import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage

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
    #it take the location and get the row-50 to row+50 and the same for the column with the color values the same
    earth = grey_image[location[0]-50:location[0]+51, location[1]-50:location[1]+51,:]

    return earth

def image_smoother(image):
    
    image=ndimage.uniform_filter(image,size=3)

def detect(image):
    xfilt=np.array([[[-1],[0],[1]],[[-2],[0],[2]],[[-1],[0],[1]]],np.float64)
    yfilt=np.array([[[1],[2],[1]],[[0],[0],[0]],[[-1],[-2],[-1]]],np.float64)
    gradx=ndimage.filters.convolve(image,xfilt,mode='constant',cval=0.0)
    grady=ndimage.filters.convolve(image,yfilt,mode='constant',cval=0.0)
    detected=np.hypot(gradx,grady)
    detected=detected/detected.max() * 255
    return detected
    
def float64_uint8(img):
    #gets the max number the data could be
    img_data_max = np.iinfo(img.dtype).max()
    img = img.astype(np.float64)/img_data_max
    img = 255*img
    img = img.astype(np.uint8)

    return img


def uint8_float64(img):
    img_data_max = np.iinfo(img.dtype).max
    img = img.astype(np.uint8)/img_data_max
    img = img.astype(np.float64)

    return img



image = plt.imread('image.tiff')[:,:,:3]
image=image/255
image = grey(image)
# image=float64_uint8(image)
# image=uint8_float64(image)
image = image_smoother(image)
# image = detect(image)
print(image)
plt.imshow(image)



# earth_location = earth_finder(image)
# print(earth_location)


# earth = earth_image(image, earth_location)
# plt.show('earth.tiff', earth)

#plt.imsave('gray.tiff', image)
