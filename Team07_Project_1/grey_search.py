"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Created user functions that convert an image to greyscale, detect the location of earth in the given image, crop the given image to 101x101 pixels, centered on the location of the earth found, blur an image, apply sobel filters to create a gradient map for edge detection, convert float64 values to uint 8, and convert uint8 values to float64.

Assignment Information
    Assignment:     Group Project
    Author:         David Gedgaud, dgedgaud@purdue.edu
                    Connor Gass, gass0@purdue.edu
                    Ashwin Limaye, limaye@purdue.edu
                    Max Drach, mdrach@purdue.edu
                    
    Team ID:        LC5 - 07

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
import Image_analysis as ia
from scipy import ndimage
def grey(image):
    
    #image = ia.image_tester(image)
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
    #grey_image = ia.image_tester(grey_image)
    
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
    

def earth_image(sharpened_image, orginal_image):
    #gets the location
    location = earth_finder(sharpened_image)
    
    #it take the location and get the row-50 to row+50 and the same for the column with the color values the same
    
    #gets the 101x101 image by take the place 0,0 as the location of the earth from the last fuction earth_finder
    #then is takes the 50 pixels, in front, above, behind and below it
    earth = orginal_image[location[0]-50:location[0]+51, location[1]-50:location[1]+51,:]

    return earth

def image_blur(image):
    
    image = uint8_float64(image)
    #image = ia.image_tester(image)
    #using the guassian filter, blurres the image
    blurred1 = scipy.ndimage.gaussian_filter(image, sigma=2.5)

    return blurred1
    
def edge_dectector(blurred_image):
    
    #no need for th absolute value since the both the x and y compnenet gonna be squared
    #gets the gradient of the blurred image in the x-direction
    sx = ndimage.sobel(blurred_image, axis=0, output=None, mode ='constant', cval=0.0)
    #gets the gradient of the blurred image in the y-direction
    sy = ndimage.sobel(blurred_image, axis=1, output=None, mode ='constant', cval=0.0)
    #hypot get the hypotenuse, or ie sqrt(a^2 + b^2) = C, this is get the gradient edge decetection
    #ie this combine the vertical and horizontal edges
    sob = np.hypot(sx, sy)
    
    sob = float64_uint8(sob)
    sob = grey(sob)
    
    return sob

def float64_uint8(img):
    #gets the max number the data could be
    #img_data_max = np.iinfo(img.dtype).max()
    #print(img_data_max)
    #img = img.astype(np.float64)/img_data_max
    #img = ia.image_tester(img)
    #times the image rgb value by 255 to get the unit8
    img = 255*img
    img = img.astype(np.uint8)

    return img


def uint8_float64(img):
    #img_data_max = np.iinfo(img.dtype).max
    #img = ia.image_tester(img)
    #dives the unint8 values to the get the 0-1 float64 values
    img = img/255
    img = img.astype(np.float64)

    return img


def test():
     image = ia.image_tester('image.tiff')
     gray = grey(image)
     plt.imsave('grey.tiff', gray)
     
     image_blurred = image_blur(gray)
     plt.imsave('blur.tiff', image_blurred)
     
     #i2 = uint8_float64(i1)
     image_edge = edge_dectector(image_blurred)
     #i2 = float64_uint8(i2)
     plt.imsave('sharp.tiff', image_edge)
     
     
     
     earth = earth_image(image_edge, image)
     plt.imsave('earth.tiff', earth)
     
    # #image = plt.imread('img_plain0.tiff')[:,:,:3]
    # image = grey(image)
    # plt.imsave('gray.tiff', image)
    
    # image2 = uint8_float64(image)
    # image2 = 
    # image2 = image_smoother(image2)
    # image2 = float64_uint8(image2)
    # image_grey = grey(image2)
    # plt.imsave('grey_sharpned.tiff', image_grey)
     
    # #earth_location = earth_finder(image_grey)
    # # print(earth_location)
    
    # earth = earth_image(,image)
    # plt.imsave('earth.tiff', earth)
 
def main():
    test()

if __name__ == '__main__':
    main()

