import numpy as np
import matplotlib.pyplot as plt
import scipy
import Image_analysis as ia
def grey(image):
    
    image = ia.image_tester(image)
    #uses matrix multiplication on the rgb values of the photo
    grey_values = (image[:,:,0]*.299 + image[:,:,1]*.587 + image[:,:,2]*.114)
    #this automatically gets the dim from the image, by just coppying
    grey = image.copy()
    
    #this inserts the grey rgb values in to the grey photo, since the rgb values should all the be same for the same row, col
    for i in range(3):
        grey[:,:,i] = grey_values

    return grey


def earth_finder(grey_image):
    #reads the string
    grey_image = ia.image_tester(grey_image)
    
    #makes sure the border exception is taken out
    grey_image = grey_image[1:,1:,:]
    
    #gets the brighest spot on the image
    brightest_spot = np.amax(grey_image)
    
    #finds the index where the maximum value is
    index_max = np.where(grey_image == brightest_spot)
   
    #takes where first items(ie earth row, earth col) of each list return, the turns the tupple to a list
    cordinates = list(zip(index_max[0], index_max[1]))
   
    #since all rgb values are the same, we only need the first item of the list
    return cordinates[0]
    

def earth_image(grey_image):
    #gets the location
    location = earth_finder(grey_image)
    
    #it take the location and get the row-50 to row+50 and the same for the column with the color values the same
    grey_image = ia.image_tester(grey_image)
    
    #gets the 101x101 image by take the place 0,0 as the location of the earth from the last fuction earth_finder
    #then is takes the 50 pixels, in front, above, behind and below it
    earth = grey_image[location[0]-50:location[0]+51, location[1]-50:location[1]+51,:]

    return earth

def image_smoother(image):
    image = ia.image_tester(image)
    #using the guassian filter,  blurred the image
    blurred1 = scipy.ndimage.gaussian_filter(image, sigma=2.5)
    
    #gets the gradient of the blurred image in the x-direction
    sx = scipy.ndimage.sobel(blurred1, axis=0, output=None, mode ='constant', cval=0.0)
    #gets the gradient of the blurred image in the y-direction
    sy = scipy.ndimage.sobel(blurred1, axis=1, output=None, mode ='constant', cval=0.0)
    #hypot get the hypotenuse, or ie sqrt(a^2 + b^2) = C, this is get the gradient edge decetection
    #ie this combine the vertical and horizontal edges
    sob = np.hypot(sx, sy)
    
    return sob

def float64_uint8(img):
    #gets the max number the data could be
    #img_data_max = np.iinfo(img.dtype).max()
    #print(img_data_max)
    #img = img.astype(np.float64)/img_data_max
    img = ia.image_tester(img)
    #times the image rgb value by 255 to get the unit8
    img = 255*img
    img = img.astype(np.uint8)

    return img


def uint8_float64(img):
    #img_data_max = np.iinfo(img.dtype).max
    img = ia.image_tester(img)
    #dives the unint8 values to the get the 0-1 float64 values
    img = img/255
    img = img.astype(np.float64)

    return img


def test():
    image = plt.imread('image.tiff')[:,:,:3]
    #image = plt.imread('img_plain0.tiff')[:,:,:3]
    image = grey(image)
    plt.imsave('gray.tiff', image)
    
    image2 = uint8_float64(image)
    image2 = image_smoother(image2)
    image2 = float64_uint8(image2)
    image_grey = grey(image2)
    plt.imsave('grey_sharpned.tiff', image_grey)
     
    earth_location = earth_finder(image_grey)
    # print(earth_location)
    
    earth = earth_image(image, earth_location)
    plt.imsave('earth.tiff', earth)
 
def main():
    pass

if __name__ == '__main__':
    main()

